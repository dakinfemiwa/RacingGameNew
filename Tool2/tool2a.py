class Cryptographer:
    def encrypt(file):
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
                        #print(letter)
                        ascIIEn = ascIINo + 2
                        decrLet = chr(ascIIEn)
                        #print(decrLet)
                        NL += decrLet
                    elif y == True:
                        if line[l:l+2] == "\n":
                            NL += "\n"
                #print(NL)
                text.append(NL)

        print(text)

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
                        #print(letter)
                        ascIIEn = ascIINo - 2
                        decrLet = chr(ascIIEn)
                        #print(decrLet)
                        NL += decrLet
                    elif y == True:
                        if line[l:l+2] == "\n":
                            NL += "\n"
                #print(NL)
                text.append(NL)

        print(text)

        with open(file, "w") as clientFile:
            for line in text:
                clientFile.write(line)
