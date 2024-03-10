from flask import Flask, request, jsonify
from datetime import datetime
import paramiko
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

def create_ssh_client(server, port, user, password):
    print(f"Creating SSH client for server: {server}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def ssh_jump_chain(username, password):
    print(f"Initiating SSH jump chain with username: {username}")
    # Connection to the first server
    client1 = create_ssh_client('ivpc1.sncrcorp.net', 22, username, password)

    # Setup for the second jump (to bastion001)
    bastion_transport = client1.get_transport()
    bastion_channel = bastion_transport.open_channel("direct-tcpip", ("bastion001.vzwtag.api.cloud.synchronoss.net", 22), ("127.0.0.1", 0))
    client2 = paramiko.SSHClient()
    client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client2.connect('bastion001.vzwtag.api.cloud.synchronoss.net', username=username, password=password, sock=bastion_channel)
    
    # Setup for the third jump (to admin001)
    admin_transport = client2.get_transport()
    admin_channel = admin_transport.open_channel("direct-tcpip", ("admin001.vzwtag.api.cloud.synchronoss.net", 22), ("127.0.0.1", 0))
    client3 = paramiko.SSHClient()
    client3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client3.connect('admin001.vzwtag.api.cloud.synchronoss.net', username=username, password=password, sock=admin_channel)
    
    return client3

def execute_command(ssh_client, command):
    print(f"Executing command: {command}")
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read()
    error = stderr.read()
    return output, error

def generate_time_pattern(start_time_str, end_time_str, time_format='%d/%b/%Y:%H:%M'):
    print(f"Generating time pattern for start: {start_time_str} and end: {end_time_str}")
    # Convert start and end times to datetime objects
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)
    
    # Generate hour and minute ranges
    start_hour = start_time.strftime('%H')
    end_hour = end_time.strftime('%H')
    
    start_minute = start_time.minute
    end_minute = end_time.minute
    
    # Assuming the range is within the same hour for simplicity
    if start_hour == end_hour:
        # Generate minute pattern
        if start_minute // 10 == end_minute // 10:  # Same ten-minute interval
            minute_pattern = f"{start_minute // 10}[{start_minute % 10}-{end_minute % 10}]"
        else:  # Different ten-minute intervals
            minute_pattern = f"({start_minute // 10}[{start_minute % 10}-9]|{end_minute // 10}[0-{end_minute % 10}])"
    else:
        # Extend this logic for ranges spanning multiple hours if needed
        minute_pattern = "UNHANDLED RANGE"  # Placeholder for more complex logic
    
    # Format the final pattern
    date_pattern = start_time.strftime('%d/%b/%Y').replace('/', '\\/')
    time_range_pattern = f"{date_pattern}:({start_hour}:{minute_pattern})"
    
    return time_range_pattern

@app.route('/tm_log_search', methods=['POST'])
def tm_log_search():
    # Extract username and password from form data
    username = request.form.get('username')
    password = request.form.get('password')
    
    print(f"Received request with username: {username}")
    
    # Extract str_to_search, start_time, and end_time from query parameters
    str_to_search = request.args.get('str_to_search')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    
    print(f"Parameters - str_to_search: {str_to_search}, start_time: {start_time}, end_time: {end_time}")
    
    # Validate inputs (basic validation)
    if not all([username, password, str_to_search, start_time, end_time]):
        print("Error: Missing required parameters")
        return jsonify({"error": "Missing username, password, or query parameter information."}), 400
    
    # Generate the time pattern
    time_pattern = generate_time_pattern(start_time, end_time)
    
    # Construct the command
    command = (
        f"find /opt/newbay/log/tm -type d -mtime -2 ! -name '*ccpa*' | "
        f"while read dir; do "
        f"find \"$dir\" -type f -name \"tagmanager_access*\" -exec "
        f"awk '/{str_to_search}/ && /({time_pattern})/' {{}} +; "
        f"done"
    )

    try:
        # Setup the SSH jumps and get the final SSH client
        final_client = ssh_jump_chain(username, password)

        # Execute the command on the final client and get the result
        output, error = execute_command(final_client, command)

        # Ensure to close the SSH client after execution
        final_client.close()

        if error:
            print("SSH command error")
            return jsonify({"error": error.decode()}), 500
        else:
            print("SSH command executed successfully")
            return jsonify({"Result": output.decode()}), 200
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
