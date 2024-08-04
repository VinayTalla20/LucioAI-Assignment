import base64 

def decodeRobotInput(encodedText):
    try:
        decodedText = base64.b64decode(encodedText).decode('utf-8', errors = 'ignore')
        return decodedText
    except:
        return None 
    
def readTxtFileFromInput(filePath):
    try:
        with open('robot.txt','r') as file:
            encryptedText = file.read().strip()
        return encryptedText
    except FileNotFoundError:
        print(f"File not found, make sure file is located at the path: {filePath}")
        return None
    except IOError as e:
        print(f"Error can not read file {e.strerror}: {filePath}")
        return None
    
def main():
    filePath = 'robot.txt'
    
    encryptedText = readTxtFileFromInput(filePath)
    
    if encryptedText:
        decodedText = decodeRobotInput(encryptedText)
        if decodedText:
            print("Ooutput of Decoded text: ", decodedText)
            
if __name__ == "__main__":
    main()
