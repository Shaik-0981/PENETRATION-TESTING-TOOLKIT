import sys
from port_scanner import scan_ports
from brute_forcer import ssh_brute_force
from vulnerability_scanner import check_sql_injection, check_xss
from network_sniffer import start_sniffing
from exploit_framework import run_exploit

def main():
    if len(sys.argv) < 2:
        print("Usage: python toolkit.py <module> <arguments>")
        sys.exit(1)

    module = sys.argv[1]

    if module == "port_scan":
        if len(sys.argv) < 4:
            print("Usage: python toolkit.py port_scan <target> <ports>")
            sys.exit(1)
        target = sys.argv[2]
        ports = [int(p) for p in sys.argv[3].split(',')]
        scan_ports(target, ports)

    elif module == "brute_force":
        if len(sys.argv) < 5:
            print("Usage: python toolkit.py brute_force <target> <username> <wordlist>")
            sys.exit(1)
        target = sys.argv[2]
        username = sys.argv[3]
        wordlist = sys.argv[4].split(',')
        ssh_brute_force(target, username, wordlist)

    elif module == "vuln_scan":
        if len(sys.argv) < 3:
            print("Usage: python toolkit.py vuln_scan <url>")
            sys.exit(1)
        url = sys.argv[2]
        check_sql_injection(url)
        check_xss(url)

    elif module == "sniff":
        start_sniffing()

    elif module == "exploit":
        if len(sys.argv) < 3:
            print("Usage: python toolkit.py exploit <target>")
            sys.exit(1)
        target = sys.argv[2]
        run_exploit(target)

    else:
        print("Invalid module. Use one of: port_scan, brute_force, vuln_scan, sniff, exploit")

if __name__ == "__main__":
    main()
