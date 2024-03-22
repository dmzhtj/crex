inpt = input("请输入。。。1.开始加密，2.开始解密,3.生成密码")

if inpt == "1":	

	text = input("明文：")
	print(text)

	ascii_codes = []
	for char in text:
    	ascii_code = ord(char)
    	ascii_codes.append(ascii_code)
	print(ascii_codes)

	while True:
    	try:
        	passwd = int(input("密码（1-2位数字）："))
        	if 0 < passwd < 100:
            	break
        	else:
            	print("密码必须为1-2位数字")
    	except ValueError:
        	print("密码必须为1-2位数字")

	for i in range(len(ascii_codes)):
    	ascii_codes[i] += passwd
	print(ascii_codes)

	encrypted_text = ''.join(chr(code) for code in ascii_codes)
	print("加密后的文本：", encrypted_text)
	print(ascii_codes)
