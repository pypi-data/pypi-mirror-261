import os
import subprocess
import sys
import pkg_resources

from infiltra.utils import (
    is_valid_ip, list_txt_files, is_valid_domain, clear_screen,
    console,
    BOLD_RED, BOLD_GREEN, BOLD_YELLOW, BOLD_WHITE, BOLD_CYAN, DEFAULT_COLOR,
    RICH_RED, RICH_YELLOW, RICH_CYAN, RICH_GREEN, RICH_COLOR
)

def check_and_install_at():
    try:
        subprocess.run(["which", "at"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        console.print("at is installed.",  style=RICH_GREEN)
    except subprocess.CalledProcessError:
        console.print("at is not installed. Installing now...",  style=RICH_YELLOW)
        install_command = "sudo apt install at -y"
        try:
            subprocess.run(install_command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            console.print("at installed successfully.",  style=RICH_GREEN)
        except subprocess.CalledProcessError as e:
            console.print(f"Failed to install at: {e}",  style=RICH_RED)
            sys.exit(1)


def run_ngrep(scan_type):
    clear_screen()
    ngrep_script_path = pkg_resources.resource_filename('infiltra', 'nmap-grep.sh')
    output_file = f"{scan_type.lower()}.txt"
    output_path = f"{scan_type.lower()}_parsed/"

    if os.path.isdir(output_path):
        overwrite = console.input(f"The directory [bold cyan]{output_path}[/bold cyan] already exists. Overwrite it? (y/n): ").strip().lower()
        if overwrite == 'y':
            subprocess.run(['rm', '-rf', output_path])
        else:
            console.print(f"Not overwriting the existing directory {output_path}.", style=RICH_COLOR)
            return

    console.print(f"Running nmap-grep.sh on {output_file} for {scan_type.upper()} scans", style=RICH_GREEN)
    subprocess.run(['bash', ngrep_script_path, output_file, scan_type.upper()])
    input(f"{BOLD_GREEN}Press Enter to return to the menu...")


def get_scheduled_scans_status(project_path):
    # Ensure there is a 'tmp' directory in the project path
    tmp_dir = os.path.join(project_path, 'tmp')
    os.makedirs(tmp_dir, exist_ok=True)

    # Check for ongoing scans by looking for marker files
    marker_file = os.path.join(tmp_dir, "nmap_scan_ongoing.marker")
    ongoing_scans = "Ongoing Scans: "
    if os.path.exists(marker_file):
        with open(marker_file, "r") as f:
            ongoing_scans += f.read()
    else:
        ongoing_scans += "None"

    # Use 'atq' to list the queued jobs and 'at -c' to inspect a specific job.
    scheduled_scans = subprocess.run(['atq'], capture_output=True, text=True)
    scheduled_scans_output = scheduled_scans.stdout if scheduled_scans.stdout else "No upcoming scans are scheduled."

    return f"{BOLD_GREEN}{ongoing_scans}\n\n{BOLD_YELLOW}Upcoming Scans:\n{scheduled_scans_output}"


def cancel_scheduled_scan():
    clear_screen()
    print(f"{BOLD_CYAN}Cancel a Scheduled Nmap Scan\n")
    # First, show all scheduled scans
    scheduled_scans = subprocess.run(['atq'], capture_output=True, text=True)
    print(scheduled_scans.stdout)

    if scheduled_scans.stdout.strip() == "":
        print(f"{BOLD_YELLOW}No scheduled scans to cancel.")
        input(f"{BOLD_GREEN}Press Enter to return to the menu...")
        return

    # Ask the user to input the job number to cancel
    job_number = input(f"{BOLD_GREEN}Enter the job number to cancel or 'x' to cancel:")
    if job_number.lower() == 'x':
        return

    # Attempt to cancel the job
    try:
        subprocess.run(['atrm', job_number], check=True)
        console.print("Scheduled scan {job_number} cancelled.",  style=RICH_YELLOW)
    except subprocess.CalledProcessError:
        console.print("Failed to cancel scheduled scan {job_number}.",  style=RICH_RED)
    input(f"{BOLD_GREEN}Press Enter to return to the menu...")


def run_nmap():
    clear_screen()

    # List the available .txt files
    txt_files = list_txt_files(os.getcwd())
    if txt_files:
        console.print("NMAP Scanner\n",  style=RICH_GREEN)
        console.print("Available .txt Files In This Project's Folder\n",  style=RICH_CYAN)
        for idx, file in enumerate(txt_files, start=1):
            print(f"{BOLD_GREEN}{idx}. {BOLD_WHITE}{file}")

    selection = input(f"{BOLD_GREEN}\nEnter a number to select a file or input a single IP address or 'x' to cancel: {BOLD_WHITE}").strip()

    if selection.isdigit() and 1 <= int(selection) <= len(txt_files):
        ip_input = txt_files[int(selection) - 1]
    elif is_valid_ip(selection) or is_valid_domain(selection):
        ip_input = selection
    else:
        print(f"{BOLD_RED}Invalid input. Please enter a valid IP address, domain, or selection number.")
        return

    scan_type = input(f"\n{BOLD_GREEN}Enter scan type (tcp/udp/both): ").lower()
    if scan_type not in ['tcp', 'udp', 'both']:
        print(f"{BOLD_RED}Invalid scan type: {scan_type}. Please enter 'tcp', 'udp', or 'both'.")
        return

    # Decide whether to run now or schedule
    action = input(f"\n{BOLD_GREEN}Do you want to run the scan now or schedule it for later? (now/later): ").lower()
    if action not in ['now', 'later']:
        print(f"{BOLD_RED}Invalid option: {action}. Please enter 'now' or 'later'.")
        return

    nmap_script_path = pkg_resources.resource_filename('infiltra', 'nmap_scan.py')
    command_string = f"sudo python3 {nmap_script_path} {ip_input} {scan_type}"

    if action == 'now':
        if scan_type in ['tcp', 'both']:
            tcp_command_string = f"echo -ne \"\\033]0;NMAP TCP\\007\"; exec {command_string} tcp"
            tcp_command = ['gnome-terminal', '--', 'bash', '-c', tcp_command_string]
            subprocess.Popen(tcp_command)
        if scan_type in ['udp', 'both']:
            udp_command_string = f"echo -ne \"\\033]0;NMAP UDP\\007\"; exec {command_string} udp"
            udp_command = ['gnome-terminal', '--', 'bash', '-c', udp_command_string]
            subprocess.Popen(udp_command)

        print(f"\n{BOLD_GREEN}Nmap {scan_type} scan launched.")
    elif action == 'later':
        date_input = input(f"{BOLD_GREEN}Enter date for the scan (mm/dd/yyyy): {BOLD_WHITE}").strip()
        time_input = input(f"{BOLD_GREEN}Enter time in military time (HHMM, e.g., 1600 for 4pm): {BOLD_WHITE}").strip()

        # Ensure time is properly formatted for the `at` command
        if len(time_input) == 3:  # If only 3 digits, add a '0' in the front
            time_input = '0' + time_input
        if ':' in time_input:
            time_input = time_input.replace(':', '')  # Remove colon

        # Combine date and time for the `at` command
        schedule_datetime = f"{time_input} {date_input}"
        at_command = f'echo "sudo python3 {nmap_script_path} {ip_input} {scan_type} True" | at {schedule_datetime}'
        try:
            at_command = f'echo "sudo python3 {nmap_script_path} {ip_input} {scan_type} True" | at {schedule_datetime}'
            subprocess.run(at_command, shell=True, check=True)
            print(f"{BOLD_GREEN}Scan scheduled for {schedule_datetime}.")
        except subprocess.CalledProcessError as e:
            print(f"{BOLD_RED}An error occurred while scheduling the scan: {e}")

    input(f"{BOLD_GREEN}Press Enter to return to the menu...")



def nmap_submenu(project_path):
    clear_screen()
    check_and_install_at()

    while True:
        clear_screen()
        console.print("NMAP Menu:\n", style=RICH_CYAN)
        print("========================================================")
        # Get the status of scheduled scans
        scheduled_scans_status = get_scheduled_scans_status(project_path)
        print(scheduled_scans_status)
        print(f"{BOLD_CYAN}========================================================\n")
        menu_options = [
            ("1. Run Scans", f"{DEFAULT_COLOR}Run or Schedule TCP and/or UDP Scans."),
            ("2. Cancel Scans", f"{DEFAULT_COLOR}Cancel scheduled scans."),
            ("3. Parse Results", f"{DEFAULT_COLOR}Parse NMAP Results.")
        ]

        for option, description in menu_options:
            print(f"{BOLD_GREEN}{option.ljust(50)}{description}")

        print(f"\n{BOLD_CYAN}Utilities:")
        print(f"{BOLD_RED}X. Return to Main Menu".ljust(50) + f"\n")

        choice = input(f"\n{BOLD_GREEN}Enter your choice: ").lower()

        if choice == '1':
            run_nmap()
        elif choice == '2':
            cancel_scheduled_scan()
        elif choice == '3':
            clear_screen()
            print(f"{BOLD_CYAN}NMAP Results Parser\n")
            scan_type = input(f"{BOLD_GREEN}Enter the scan type that you want to parse (TCP/UDP): ").upper()
            run_ngrep(scan_type)
        elif choice == 'x':
            return
        else:
            print(f"{BOLD_YELLOW}Invalid choice, please try again.")
            input(f"{BOLD_GREEN}Press Enter to continue...")


if __name__ == '__main__':
    nmap_submenu(os.getcwd())
