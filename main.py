## Extract Page Source from Javascript Rendered Webpage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

## Extract email data from html page source string
import re
from bs4 import BeautifulSoup

def get_csvlist(__fullpath):
    try:
        with open(__fullpath, "r+", encoding='iso-8859-1') as __f:  ## encoding='UTF-8'
            __list = list(__f)
            __f.close()
            __converted_list = []
            __item_count = 0
            for __i in __list:
                __converted_list.append(__i.strip())
                __item_count += 1
            print('[+] INFO: total lines: ' + str(__item_count))
            return __converted_list
    except:
        print("[+] ERROR: file not found " + str(__fullpath))
        sys.exit()
        return []

def parse(__string,__first_str_delimiter, __second_str_delimiter):
    __mystring = ""
    first_delimiter_detected = False
    pattern_length = len(__first_str_delimiter)
    new_pattern = ""
    for __i in range(pattern_length):
        new_pattern = new_pattern + " "
    ####
    second_delimiter_detected = False
    endpattern_length = len(__second_str_delimiter)
    second_new_pattern = ""
    for __i in range(endpattern_length):
        second_new_pattern = second_new_pattern + " "
    ###

    __data_str = ""
    __data_str2 = ""
    str_length = len(__string)
    for __i in range(str_length):

        if (__data_str == __first_str_delimiter):
            first_delimiter_detected = True

        char = __string[__i]

        if (len(__data_str) == pattern_length):
            __data_str = __data_str[1:]
            __data_str = __data_str + char
        else:
            __data_str = __data_str + char
        #print(__data_str) ## for debug

        if (first_delimiter_detected == True):

            if (len(__data_str2) == endpattern_length):

                if (__data_str2 == __second_str_delimiter):
                    second_delimiter_detected = True
                    break

                new_char = __data_str2[:1]
                __data_str2 = __data_str2[1:]
                __data_str2 = __data_str2 + char

                if (second_delimiter_detected == False):
                    __mystring = __mystring + new_char
            else:
                __data_str2 = __data_str2 + char

    return __mystring

def save_data(company, website, email):
    global output_name
    # Output file path
    output_file_path = output_name

    # Check if the file exists
    file_exists = os.path.isfile(output_file_path)

    # Open the output CSV file in append mode, create it if it doesn't exist
    with open(output_file_path, 'a', newline='', encoding='utf-8') as output_file:
        # If the file doesn't exist, write the header
        if not file_exists:
            output_file.write('Company,Website,Email\n')

        # Write the data to the output CSV file
        output_file.write(f"{company},{website},{email}\n")

        # Print the added data
        print(f"Adding to {output_name}: {company}, {website}, {email}")

def clean_data(input_string):
    # Define the delimiters
    start_delimiter = 'mailto:'
    end_delimiter = '">'

    # Find the start and end indices
    start_index = input_string.find(start_delimiter)
    end_index = input_string.find(end_delimiter, start_index)

    # Extract the substring between the delimiters
    if start_index != -1 and end_index != -1:
        extracted_email = input_string[start_index + len(start_delimiter):end_index]
        return extracted_email
    else:
        return "No email found"


__listlist = []
binary_location_path=""
chrome_driver_path = ""
output_name = ""
__list = get_csvlist("config.txt")
for __i in range(0, len(__list)):
    __split = __list[__i].split("=")
    __listlist.append(__split)

for __i in range(0, len(__listlist)):
    if(__listlist[__i][0] == "filename"):
        file_path = __listlist[__i][1]
    if(__listlist[__i][0] == "chrome_driver_path"):
        binary_location_path = __listlist[__i][1]
    if(__listlist[__i][0] == "google_browser_path"):
        chrome_driver_path = __listlist[__i][1]
    if(__listlist[__i][0] == "output_name"):
        output_name = __listlist[__i][1]


opt = webdriver.ChromeOptions()
# opt.binary_location = r"D:\bin\google\Chrome\Application\chrome.exe"
# chrome_driver_path = Service(r"D:\bin\driver\chromedriver.exe")
opt.binary_location = binary_location_path
chrome_driver_path = Service(chrome_driver_path)
opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
opt.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging']) ## Removing Navigator.Webdriver Flag ::: navigator.webdriver

# Start a Selenium WebDriver (make sure to download the appropriate webdriver for your browser)
driver = webdriver.Chrome(options=opt, service=chrome_driver_path)
driver.set_window_position(0,0)
driver.set_window_size(900,720) ## android Standard HD resolution
driver.set_page_load_timeout(1800)


# Open the CSV file
with open(file_path, 'r', encoding='utf-8') as file:
    # Skip the header
    header = next(file)

    # Get the total number of lines in the file
    total_lines = sum(1 for _ in file)

    # Return to the beginning of the file
    file.seek(0)

    # Skip the header again
    next(file)

    # Iterate over each line in the CSV file
    for current_line, line in enumerate(file, start=1):
        # Split the line into columns
        columns = line.strip().split(',')

        company_data = columns[0].strip('"')

        # Extract the website data from the second column
        website_data = columns[1].strip('"')

        if not (website_data == ""):
            # Print the status and website data
            print(f"{current_line}/{total_lines} - Website:", website_data)

            site = website_data
            retry=0
            email_match = ""
            while True:
                try:
                    if(retry >= 3):
                        break
                    # Open the URL of the JavaScript-rendered page
                    driver.get(website_data)

                    # Scroll to the bottom of the page to ensure all JavaScript is loaded
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)  # Adjust the sleep time based on your page loading time

                    # Wait for the page to fully load (you might need to adjust the waiting time based on your page)
                    driver.implicitly_wait(3)

                    # Get the HTML source after JavaScript rendering
                    html_source = driver.page_source

                    # ex = multi_instance_parse(html_source,"mailto:", '">')

                    ex = parse(html_source,"mailto:", '"')


                    email_match = ex
                    if(email_match.find("@")>0):
                        if len(email_match) >= 30:
                            ex = parse(html_source,"mailto:", '?')
                            mail_match = ex
                            if(email_match.find("@")>0):
                                if len(email_match) >= 30:
                                    email_match = "No email found"
                        break
                    else:
                        retry+=1
                        time.sleep(1)
                        if(retry==1):
                            website_data = website_data + "/contact"
                    # break

                except Exception as e:
                    retry+=1
                    time.sleep(1)
                    # print(e)
                    print("trying...")
                    if(retry==1):
                        website_data = website_data + "/contact"
                    pass

            # email_address = clean_data(str(email_match))
            email_address = email_match
            if email_address:
                print("Extracted Email Address:", email_address)
                save_data(company_data,site,email_address)
            else:
                print("No email address found.")
                save_data(company_data,site,"No email found")
        else:
            print(f"{current_line}/{total_lines} - Visiting Website:", "not found!")
            save_data(company_data,site,"No email found")

# Close the WebDriver
driver.quit()
