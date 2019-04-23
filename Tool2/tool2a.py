class Cryptographer:
    def encrypt(file):
        global text
        text = []

        with open(file, "r") as clientFile:
            lines = clientFile.readlines()
            for line in lines:
                NL = ""
                for l in range(0, len(line)):
                    letter = line[l]
                    y = False
                    if line[l:l+2] == "\n" or line[l-2:l] == "\n":
                        y = True

                    if y == False:
                        ascIINo = ord(letter)
                        ascIIEn = ascIINo + 2
                        decrLet = chr(ascIIEn)
                        NL += decrLet
                    elif y == True:
                        if line[l:l+2] == "\n":
                            NL += "\n"
                            
                text.append(NL)


        with open(file, "w") as clientFile:
            for line in text:
                clientFile.write(line)

    def decrypt(file):
        global text
        text = []

        with open(file, "r") as clientFile:
            lines = clientFile.readlines()
            print(lines)
            for line in lines:
                NL = ""
                for l in range(0, len(line)):
                    letter = line[l]
                    y = False
                    if line[l:l+2] == "\n" or line[l-2:l] == "\n":
                        y = True

                    if y == False:
                        ascIINo = ord(letter)
                        ascIIEn = ascIINo - 2
                        decrLet = chr(ascIIEn)
                        NL += decrLet
                    elif y == True:
                        if line[l:l+2] == "\n":
                            NL += "\n"
                text.append(NL)


        with open(file, "w") as clientFile:
            for line in text:
                clientFile.write(line)
