#define classes

class encrypt():
  def __init__(self,ptext,shift):
      self.ptext = str(ptext)
      self.shift = int(shift)%26
  
  def encrypt(self):
    self.encmsg = ''
    for char in self.ptext:
      a = ord(char)
      b = a + self.shift

      if b < 65:
        b += 26
      elif b <= 90 and a <= 90:
        pass
      elif b <= 90 and a > 90:
        b += 26
      elif b < 97 and a <= 90:
        b -= 26
      elif b < 97 and a > 90:
        b += 26
      elif b <= 122:
        pass
      else:
        b -= 26

      self.encmsg += chr(b)

    return self.encmsg


class decrypt():
  def __init__(self,encmsg,shift):
      self.encmsg = str(encmsg)
      self.shift = int(shift)%26
  
  def decrypt(self):
    self.ptext = ''
    for char in self.encmsg:
      a = ord(char)
      b = a - self.shift

      if b < 65:
        b += 26
      elif b <= 90 and a <= 90:
        pass
      elif b <= 90 and a > 90:
        b += 26
      elif b < 97 and a <= 90:
        b -= 26
      elif b < 97 and a > 90:
        b += 26
      elif b <= 122:
        pass
      else:
        b -= 26

      self.ptext += chr(b)

    return self.ptext

#create user inputs and output

if input("do you want to encrypt(e) or decrypt(d). Type e or d : ") == 'e':
  msg = encrypt(input("type your plain text : ") , input("type the shift value (integer) : "))
  print("the encrypted message is " + msg.encrypt())
else:
  msg = decrypt(input("type your ecncrypted text : ") , input("type the shift value (integer) : "))
  print("the decrypted message is " + msg.decrypt())
