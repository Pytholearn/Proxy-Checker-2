import requests
import time
import AutoUpdate

AutoUpdate.set_url("https://raw.githubusercontent.com/Pytholearn/Proxy-Checker-2/refs/heads/main/version")
AutoUpdate.set_current_version("1.4.7")
AutoUpdate.set_download_link("https://github.com/Pytholearn/Proxy-Checker-2.git")

if not AutoUpdate.is_up_to_date():
    print("Would you like to update your tool?")
    choice = input("Enter (y/n): ")
    if choice == "y":
        AutoUpdate.update()
    else:
        pass
            
with open("http_proxies.txt", "r") as file:
    proxies_list = [line.strip() for line in file if line.strip()]

error_list = 0
good_list = 0


ip_check_url = "http://api.ipify.org"  
with open("good_proxies.txt", "w") as good_file:
    
    for index, proxy in enumerate(proxies_list, start=1):
        proxies = {"http": proxy, "https": proxy}
        
        try:
            
            response = requests.get(ip_check_url, proxies=proxies, timeout=10)
            
            
            if response.status_code == 200:
                good_list += 1
                print(f"{index}/{len(proxies_list)} ✅ Proxy: {proxy} - IP: {response.text} - Good: {good_list} - Bad: {error_list}")
                good_file.write(proxy + "\n")  
            else:
                error_list += 1
                print(f"{index}/{len(proxies_list)} ❌ Proxy: {proxy} - Status: {response.status_code} - Good: {good_list} - Bad: {error_list}")
        
        
        except requests.exceptions.Timeout:
            error_list += 1
            print(f"{index}/{len(proxies_list)} ⏱️ Timeout Error: {proxy} - Good: {good_list} - Bad: {error_list}")
        except requests.exceptions.ProxyError:
            error_list += 1
            print(f"{index}/{len(proxies_list)} 🔌 Proxy Error: {proxy} - Good: {good_list} - Bad: {error_list}")
        except requests.exceptions.RequestException as e:
            error_list += 1
            print(f"{index}/{len(proxies_list)} ⚠️ Other Error: {proxy} - {str(e)} - Good: {good_list} - Bad: {error_list}")
        
        
        time.sleep(2)


print(f"\n🔍 Good Proxy: {good_list} - Bad Proxy: {error_list}")
