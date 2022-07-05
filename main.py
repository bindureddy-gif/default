# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  requests;
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getUsers() :
    data = requests.get("https://randomuser.me/api/")
    print("response", data.text.r)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    getUsers();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


