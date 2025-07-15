import requests
import json
import webbrowser
import os
import platform
from ipaddress import ip_address
from colorama import init, Fore, Back, Style
import time


init(autoreset=True)

BANNER = f"""
{Fore.GREEN}██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
{Fore.GREEN}██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
{Fore.WHITE}██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
{Fore.WHITE}██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
{Fore.RED}██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
{Fore.RED}╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

{Fore.MAGENTA}███████╗ █████╗ ██████╗ ██╗    ██╗██╗  ██╗
{Fore.CYAN}██╔════╝██╔══██╗██╔══██╗██║    ██║╚██╗██╔╝
{Fore.GREEN}███████╗███████║██║  ██║██║ █╗ ██║ ╚███╔╝ 
{Fore.GREEN}╚════██║██╔══██║██║  ██║██║███╗██║ ██╔██╗ 
{Fore.MAGENTA}███████║██║  ██║██████╔╝╚███╔███╔╝██╔╝ ██╗
{Fore.MAGENTA}╚══════╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝
{Style.RESET_ALL}"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_telegram():
    telegram_url = "https://t.me/sadwxtm"
    print(f"\n{Fore.CYAN}Opening Telegram channel...{Style.RESET_ALL}")
    try:
        if platform.system() == "Linux" and "android" in platform.platform().lower():
            os.system(f"am start -a android.intent.action.VIEW -d {telegram_url}")
        else:
            webbrowser.open(telegram_url)
    except Exception as e:
        print(f"{Fore.RED}Failed to open Telegram: {e}{Style.RESET_ALL}")

def animate_loading(message="Loading", duration=2):
 
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            print(f"\r{Fore.CYAN}{char} {message}...{Style.RESET_ALL}", end="", flush=True)
            time.sleep(0.1)
    print(f"\r{Fore.GREEN}✓ {message} complete!{Style.RESET_ALL}")

def validate_ip(ip):

    try:
        ip_obj = ip_address(ip)
        if ip_obj.is_private:
            print(f"{Fore.YELLOW}[!] Warning: This is a private IP address{Style.RESET_ALL}")
        elif ip_obj.is_loopback:
            print(f"{Fore.YELLOW}[!] Warning: This is a loopback address{Style.RESET_ALL}")
        elif ip_obj.is_multicast:
            print(f"{Fore.YELLOW}[!] Warning: This is a multicast address{Style.RESET_ALL}")
        return True
    except ValueError:
        return False

def get_enhanced_ip_info(ip, full_info=False):

    try:
        if not validate_ip(ip):
            print(f"{Fore.RED}[!] Error: Invalid IP address format{Style.RESET_ALL}")
            return
        
        animate_loading("Gathering IP information")
        

        fields = "status,message,query,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting"
        if full_info:
            fields = "status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        
        response = requests.get(f"http://ip-api.com/json/{ip}?fields={fields}", timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{Fore.GREEN}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║{Fore.YELLOW}                    IP INFORMATION FOR {ip}                     {Fore.GREEN}║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
            

            print(f"\n{Fore.CYAN}┌─────────────────────{Fore.WHITE} LOCATION DETAILS {Fore.CYAN}─────────────────────┐")
            print(f"{Fore.CYAN}│{Fore.WHITE} Country      : {Fore.GREEN}{data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f"{Fore.CYAN}│{Fore.WHITE} Region       : {Fore.GREEN}{data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
            print(f"{Fore.CYAN}│{Fore.WHITE} City         : {Fore.GREEN}{data.get('city', 'N/A')}")
            print(f"{Fore.CYAN}│{Fore.WHITE} ZIP Code     : {Fore.GREEN}{data.get('zip', 'N/A')}")
            print(f"{Fore.CYAN}│{Fore.WHITE} Coordinates  : {Fore.GREEN}{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
            print(f"{Fore.CYAN}│{Fore.WHITE} Timezone     : {Fore.GREEN}{data.get('timezone', 'N/A')}")
            
            if full_info:
                print(f"{Fore.CYAN}│{Fore.WHITE} Continent    : {Fore.GREEN}{data.get('continent', 'N/A')} ({data.get('continentCode', 'N/A')})")
                print(f"{Fore.CYAN}│{Fore.WHITE} District     : {Fore.GREEN}{data.get('district', 'N/A')}")
                print(f"{Fore.CYAN}│{Fore.WHITE} Currency     : {Fore.GREEN}{data.get('currency', 'N/A')}")
                print(f"{Fore.CYAN}│{Fore.WHITE} UTC Offset   : {Fore.GREEN}{data.get('offset', 'N/A')}")
            
            print(f"{Fore.CYAN}└──────────────────────────────────────────────────────────────────────┘")
            

            print(f"\n{Fore.MAGENTA}┌─────────────────────{Fore.WHITE} NETWORK DETAILS {Fore.MAGENTA}─────────────────────┐")
            print(f"{Fore.MAGENTA}│{Fore.WHITE} ISP          : {Fore.GREEN}{data.get('isp', 'N/A')}")
            print(f"{Fore.MAGENTA}│{Fore.WHITE} Organization : {Fore.GREEN}{data.get('org', 'N/A')}")
            print(f"{Fore.MAGENTA}│{Fore.WHITE} AS Number    : {Fore.GREEN}{data.get('as', 'N/A')}")
            
            if full_info:
                print(f"{Fore.MAGENTA}│{Fore.WHITE} AS Name      : {Fore.GREEN}{data.get('asname', 'N/A')}")
                print(f"{Fore.MAGENTA}│{Fore.WHITE} Reverse DNS  : {Fore.GREEN}{data.get('reverse', 'N/A')}")
            
            print(f"{Fore.MAGENTA}└──────────────────────────────────────────────────────────────────────┘")
            
            # Security Information
            print(f"\n{Fore.BLUE}┌─────────────────────{Fore.WHITE} SECURITY ANALYSIS {Fore.BLUE}─────────────────────┐")
            mobile_status = "Yes" if data.get('mobile', False) else "No"
            proxy_status = "Yes" if data.get('proxy', False) else "No"
            hosting_status = "Yes" if data.get('hosting', False) else "No"
            
            print(f"{Fore.BLUE}│{Fore.WHITE} Mobile       : {Fore.GREEN}{mobile_status}")
            print(f"{Fore.BLUE}│{Fore.WHITE} Proxy/VPN    : {Fore.GREEN}{proxy_status}")
            print(f"{Fore.BLUE}│{Fore.WHITE} Hosting      : {Fore.GREEN}{hosting_status}")
            print(f"{Fore.BLUE}└──────────────────────────────────────────────────────────────────────┘")
            
            # Google Maps integration
            lat = data.get('lat')
            lon = data.get('lon')
            if lat and lon:
                maps_url = f"https://www.google.com/maps/place/{lat},{lon}"
                print(f"\n{Fore.YELLOW}[+] Google Maps Location: {Fore.CYAN}{maps_url}{Style.RESET_ALL}")
                
                open_map = input(f"\n{Fore.YELLOW}[?] Open location in Google Maps? (y/n): {Style.RESET_ALL}").lower()
                if open_map == 'y':
                    webbrowser.open(maps_url)
            
            print(f"\n{Fore.GREEN}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║{Fore.YELLOW}                    TRACKING COMPLETED SUCCESSFULLY                  {Fore.GREEN}║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
            
        else:
            print(f"{Fore.RED}[!] Error: {data.get('message', 'Unknown error')}{Style.RESET_ALL}")
            
    except ValueError:
        print(f"{Fore.RED}[!] Error: Invalid IP address format{Style.RESET_ALL}")
    except requests.RequestException as e:
        print(f"{Fore.RED}[!] Error: Failed to connect to IP API - {str(e)}{Style.RESET_ALL}")
    except json.JSONDecodeError:
        print(f"{Fore.RED}[!] Error: Invalid response from server{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Unexpected error: {str(e)}{Style.RESET_ALL}")

def get_my_ip():
    """Get current public IP address"""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=10)
        data = response.json()
        return data.get('ip', None)
    except:
        try:
            response = requests.get("https://httpbin.org/ip", timeout=10)
            data = response.json()
            return data.get('origin', None)
        except:
            return None

def show_menu():

    print(f"\n{Fore.CYAN}┌─────────────────────────{Fore.WHITE} MENU {Fore.CYAN}─────────────────────────┐")
    print(f"{Fore.CYAN}│{Fore.YELLOW} [0] {Fore.WHITE}- Get My IP Address & Information")
    print(f"{Fore.CYAN}│{Fore.YELLOW} [1] {Fore.WHITE}- Track IP Address (Basic Info)")
    print(f"{Fore.CYAN}│{Fore.YELLOW} [2] {Fore.WHITE}- Track IP Address (Full Info)")
    print(f"{Fore.CYAN}│{Fore.YELLOW} [3] {Fore.WHITE}- Open Telegram Channel")
    print(f"{Fore.CYAN}│{Fore.YELLOW} [4] {Fore.WHITE}- Exit")
    print(f"{Fore.CYAN}└──────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")

def main():

    while True:
        clear_screen()
        print(BANNER)
        print(f"{Fore.WHITE}                    {Fore.CYAN}Advanced IP Geolocation Tool")
        print(f"{Fore.WHITE}                    {Fore.YELLOW}Created by SADWX Team")
        print(f"{Fore.WHITE}                    {Fore.GREEN}Telegram: @sadwxtm")
        
        show_menu()
        
        choice = input(f"\n{Fore.YELLOW}[?] Select an option: {Style.RESET_ALL}").strip()
        
        if choice == "0":
            print(f"\n{Fore.CYAN}[*] Getting your IP address...{Style.RESET_ALL}")
            my_ip = get_my_ip()
            if my_ip:
                print(f"\n{Fore.GREEN}[+] Your IP Address: {Fore.CYAN}{my_ip}{Style.RESET_ALL}")
                get_enhanced_ip_info(my_ip, full_info=True)
            else:
                print(f"{Fore.RED}[!] Could not determine your IP address{Style.RESET_ALL}")
        
        elif choice == "1":
            ip = input(f"\n{Fore.YELLOW}[?] Enter IP address to track: {Style.RESET_ALL}").strip()
            if ip:
                get_enhanced_ip_info(ip, full_info=False)
            else:
                print(f"{Fore.RED}[!] Please enter a valid IP address{Style.RESET_ALL}")
        
        elif choice == "2":
            ip = input(f"\n{Fore.YELLOW}[?] Enter IP address for full tracking: {Style.RESET_ALL}").strip()
            if ip:
                get_enhanced_ip_info(ip, full_info=True)
            else:
                print(f"{Fore.RED}[!] Please enter a valid IP address{Style.RESET_ALL}")
        
        elif choice == "3":
            open_telegram()
        
        elif choice.lower() in ["4", "exit", "quit"]:
            print(f"\n{Fore.YELLOW}Thanks for using IP-Tracker SADWX!{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Join our Telegram: {Fore.CYAN}@sadwxtm{Style.RESET_ALL}")
            break
        
        else:
            print(f"{Fore.RED}[!] Invalid option. Please try again.{Style.RESET_ALL}")
        
        # Wait for user input before continuing
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Program interrupted by user{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Thanks for using IP-Tracker SADWX!{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] An unexpected error occurred: {str(e)}{Style.RESET_ALL}")
