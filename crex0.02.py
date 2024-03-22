import unicodedata

def encrypt_text():
    text = input("请输入明文中文文本：")
    print(text)

    # Convert Chinese characters to Unicode code points
    code_points = [ord(char) for char in text]
    print("Unicode编码点: ", code_points)

    while True:
        try:
            passwd = int(input("请输入密码（1-2位数字）（若出现方块，可调小密码）："))
            if 0 < passwd < 100:
                break
            else:
                print("密码必须为1-2位数字")
        except ValueError:
            print("密码必须为1-2位数字")

    # Perform encryption by adding the password to each code point
    encrypted_code_points = [code + passwd for code in code_points]
    print("加密后的编码点：", encrypted_code_points)

    # Convert the encrypted code points back to characters
    encrypted_text = ''.join(chr(code) for code in encrypted_code_points)
    print("加密后的文本：", encrypted_text)

def decrypt_text():
    # Add code for decryption here
    pass

def generate_password():
    # Add code for password generation here
    pass

selected_option = input("请输入选项：1.开始加密，2.开始解密, 3.生成密码：")
if selected_option == "1":
    encrypt_text()
elif selected_option == "2":
    decrypt_text()
elif selected_option == "3":
    generate_password()
else:
    print("无效选项")
