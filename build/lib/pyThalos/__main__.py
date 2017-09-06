import argparse

from . import user

parser = argparse.ArgumentParser()
parser.add_argument("remote", help="Thalos server address")
parser.add_argument("port", help=" Thalos server port")
parser.add_argument("action", help="Register | Login | GenerateMasterKey | newBasket | deleteBasket basketname | List basketname | Download basketname filename | Delete basketname filename | Upload basketname")
parser.add_argument("-u", "--username", help="Account username")
parser.add_argument("-m", "--email", help="Account email address")
parser.add_argument("-p", "--password", help="Account Password. \n Beware, using this flag your password will be logged by your system. If left blank you will be prompted for password when needed")
parser.add_argument("-b", "--masterpassphrase", help="Master passphrase \n Beware, using this flag your password will be logged by your system. If left blank you will be prompted for password when needed")
parser.add_argument("-k", "--masterkey", help="Your masterkey")
parser.add_argument("-bk", "--bmasterkey", help="basker master key")
parser.add_argument("-bp", "--basketpassphrase", help="Basket passphrase \n Beware, using this flag your password will be logged by your system. If left blank you will be prompted for password when needed")

def main():
    args = parser.parse_args()

    if(args.action == "Register"):
        remote_address = args.remote+":"+args.port+"/api/user/signup"
        user.remotecreateuser(remote_address, args.username, args.email, args.password)


main()
