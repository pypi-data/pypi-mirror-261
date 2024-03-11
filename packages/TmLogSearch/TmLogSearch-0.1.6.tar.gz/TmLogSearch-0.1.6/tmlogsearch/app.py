from flask import Flask, request, jsonify, render_template, abort
from datetime import datetime, timedelta
import paramiko
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Global variable to store SSH clients
ssh_clients = {}

def create_ssh_client(server, port, user, password):
    print(f"Creating SSH client for server: {server}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def establish_ssh_connections(username, password):
    global ssh_clients
    
    # Connection to the first server
    client1 = create_ssh_client('ivpc1.sncrcorp.net', 22, username, password)
    ssh_clients['server1'] = client1
    
    # Setup for the second jump (to bastion001)
    bastion_transport = client1.get_transport()
    bastion_channel = bastion_transport.open_channel("direct-tcpip", ("bastion001.vzwtag.api.cloud.synchronoss.net", 22), ("127.0.0.1", 0))
    client2 = paramiko.SSHClient()
    client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client2.connect('bastion001.vzwtag.api.cloud.synchronoss.net', username=username, password=password, sock=bastion_channel)
    ssh_clients['server2'] = client2
    
    # Setup for the third jump (to admin001)
    admin_transport = client2.get_transport()
    admin_channel = admin_transport.open_channel("direct-tcpip", ("admin001.vzwtag.api.cloud.synchronoss.net", 22), ("127.0.0.1", 0))
    client3 = paramiko.SSHClient()
    client3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client3.connect('admin001.vzwtag.api.cloud.synchronoss.net', username=username, password=password, sock=admin_channel)
    ssh_clients['server3'] = client3

def execute_command(ssh_client, command):
    print(f"Executing command: {command}")
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read()
    error = stderr.read()
    print(f"grep result :{output.decode()}")
    return output, error

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/establish_ssh_connection', methods=['POST'])
def establish_ssh_connection():
    username = request.form.get('username')
    password = request.form.get('password')
    
    print(f"Establishing SSH connection for user: {username}")
    try:
        establish_ssh_connections(username, password)
        return jsonify({"message": "SSH connections established successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/close_ssh_connection', methods=['POST'])
def close_ssh_connection():
    global ssh_clients
    try:
        for client in ssh_clients.values():
            client.close()
        ssh_clients = {}
        return jsonify({"message": "SSH connections closed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_time_per_hr_pattern(start_time_str, end_time_str, time_format='%d/%b/%Y:%H:%M'):
    print(f"Generating generate_time_per_hr_pattern time pattern for start: {start_time_str} and end: {end_time_str}")
    # Convert start and end times to datetime objects
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)
    
    # Ensure both times are within the same hour for this logic
    if start_time.strftime('%Y%m%d%H') != end_time.strftime('%Y%m%d%H'):
        return "UNHANDLED RANGE: Time range spans multiple hours."
    
    # Generate patterns covering the entire range of minutes
    pattern_parts = []
    for minute in range(start_time.minute, end_time.minute + 1):
        ten_minute_group = minute // 10
        single_minute = minute % 10
        pattern_parts.append(f"{ten_minute_group}{single_minute}")

    # Deduplicate and sort the minute patterns to ensure we cover each minute range efficiently
    pattern_parts = sorted(set(pattern_parts))

    # Combine adjacent patterns where possible to simplify the regex
    combined_patterns = '|'.join(pattern_parts)

    # Construct the final pattern
    date_pattern = start_time.strftime('%d/%b/%Y:').replace('/', '\\/')
    time_range_pattern = f"{date_pattern}{start_time.strftime('%H')}:({combined_patterns})"
    
    return time_range_pattern

def generate_time_chunks(start_time, end_time):
    start_datetime = datetime.strptime(start_time, '%d/%b/%Y:%H:%M')
    end_datetime = datetime.strptime(end_time, '%d/%b/%Y:%H:%M')

    time_chunks = []

    while start_datetime < end_datetime:
        next_hour = start_datetime.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        if next_hour > end_datetime:
            next_hour = end_datetime
        if next_hour.minute == 0:
            next_hour -= timedelta(seconds=1)  # Adjusting to end at 59th minute if it's a full hour
        time_chunks.append({'start_time': start_datetime.strftime('%d/%b/%Y:%H:%M'),
                            'end_time': next_hour.strftime('%d/%b/%Y:%H:%M')})
        start_datetime = next_hour + timedelta(seconds=1)  # Adding one second to avoid overlap

    return time_chunks

@app.route('/tm_log_search', methods=['POST'])
def tm_log_search():
    # Extract str_to_search, start_time, and end_time from query parameters
    str_to_search = request.args.get('str_to_search')
    start_time_str = request.args.get('start_time')
    end_time_str = request.args.get('end_time')
    
    # Check if seconds are present in start_time_str and end_time_str
    if ':' in start_time_str and len(start_time_str.split(':')) > 3:
        start_time_format = '%d/%b/%Y:%H:%M:%S'
    else:
        start_time_format = '%d/%b/%Y:%H:%M'

    if ':' in end_time_str and len(end_time_str.split(':')) > 3:
        end_time_format = '%d/%b/%Y:%H:%M:%S'
    else:
        end_time_format = '%d/%b/%Y:%H:%M'
    # Validate str_to_search
    if not str_to_search:
        return jsonify({"error": "'str_to_search' parameter cannot be empty."}), 400
    
    
    # Parse start_time_str and end_time_str into datetime objects
    start_time_1 = datetime.strptime(start_time_str, start_time_format)
    end_time_1 = datetime.strptime(end_time_str, end_time_format)
    
    # Validate maximum duration
    max_duration = timedelta(hours=2)
    duration = end_time_1 - start_time_1
    if duration > max_duration:
        return jsonify({"error": "Maximum duration between start time and end time should not exceed 2 hours"}), 400
    # Validate minimum duration
    min_duration = timedelta(minutes=1)
    if duration < min_duration:
        return jsonify({"error": "Minimum duration between start time and end time is 1 minute"}), 400

    # Convert start_time and end_time back to strings without seconds
    start_time = start_time_1.strftime('%d/%b/%Y:%H:%M')
    end_time = end_time_1.strftime('%d/%b/%Y:%H:%M')       

    print(f"Searching logs for string: {str_to_search}")

    try:
        if not ssh_clients:
            return jsonify({"error": "SSH connections not established"}), 500
        
        time_chunks = generate_time_chunks(start_time, end_time)
        final_pattern = ""
        for i, chunk in enumerate(time_chunks):
            print("Start time:", chunk['start_time'])
            print("End time:", chunk['end_time'])
            print()
            final_pattern += generate_time_per_hr_pattern(chunk['start_time'], chunk['end_time'])
            if i != len(time_chunks) - 1:
                final_pattern += '|'
            print(final_pattern)

        
        # Construct the command
        command = (
            f"find /opt/newbay/log/tm -mindepth 1 -type d -mtime -8 ! -name '*ccpa*' -execdir sh -c '"
            f"for file in \"$1\"/tagmanager_access*; do "
            f"awk \"/{str_to_search}/ && /({final_pattern})/\" \"$file\"; "
            f"done "
            f"' sh {{}} \\; | sort | uniq"
        )

        # Execute command on the last server in the SSH chain
        output, error = execute_command(ssh_clients['server3'], command)
        
        if error:
            print("SSH command error")
            return jsonify({"error": error.decode()}), 500
        else:
            print("SSH command executed successfully")
            return jsonify({"Result": output.decode()}), 200
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
