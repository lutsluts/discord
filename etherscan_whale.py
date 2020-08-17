from selenium import webdriver
import xpath, time, pprint

PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# enter your whale addresses here, dont forget spaces inbetween addresses
ids = """
0x660b089ada54c6223805fd71ac9fb60d83792a60 0xe20b14e2ab32ba51594710279c0ddbd8b3acdeac 0x5701a77d4cddcbaddc6dce14d18d0335132e3acd 0xc1a29ff039e430f613e96be5f3559f734597b1b0
0x9085610ddb7154666c36b09c3748966f88ca5f89 0x02528db0b47608bb37c554731c847add29071779 0x9be1a4e37184d35e08bb3f9c56c874e617d8c8ce 0xfa8cf4e627698c5d5788abb7880417e75023139
0xda4a4626d3e16e094de3225a751aab7128e96526 0x70f61dc2c905d3ac56490700dd4af670ac9d4870 0x9f42587bf99dd4c25a6dc47a8e9c90196ec2c52d 0x56c1533ea530aa1c61fe1bf4dcd7c234d52602b2
0xac21d0382b34021c11d53f7dc44a3778db87e5cd 0x4ef2ab73ef2214ebeba6f087a8dcf89731504301 0x25dc9a4df709ff226708914572ba401b9220ccb3 0x75520ce0da2be5926f54578c341d5d68b201e8b5
0xef1e09e3691ad93ff80555c4da5958fef88d0da3 0x2876d8e7112572a5f60432b74af3d423d8b50cdf 0x929e339923dc0f499c3eb465ee156b89cdb3c867 0x57f303305571976f8445096becf81638d0467f42
0x2876d8e7112572a5f60432b74af3d423d8b50cdf 0xc863b3019b272b1581441ae0fe7a85983bcfda81 0x1b75fc349ef2344c4d4aa805bee93177efd10bca 0x45ef91cc7fd3bbb37f59d23ea04370a15a2a5407
0x38a8a554190447b37064c7aba2d3fd4b4d19a642 0xdf40e32c9a1e045abdf049b48007e8e08602d443 0x9e82f421dc0f59383a63bbeb1273560193fd47b1 0x20fd18258b188c0db6d6441bace19081c07d3f4d
0x538121b30582774b85bc499eef0a6a37c2bc25c7 0x9e6dd847357f7c392f78928f2a202ab10f3de653 0xff72042e258dc6676312831f8b6240ef2e06df22 0x24b6fd519431d567b7395a8c169e82205602756b
0x89bbc7384e3efba168b13faa342c13faf1cd4314 0x0a559ac111e26a44f9b49a31359a94d8ef190aea 0x4aa8b525701f3feb959cece6d66ecdeca32d593c 0xfd71516a2cfe3b297176425edb4f19babce4f916
"""



ids = ids.split(" ")
#pprint.pprint(ids)
#uncomment for printing
start = time.time()

for i in range(len(ids)):
  count = 0 # found wallets
  driver.get("https://etherscan.io/tokentxns?a={}".format(ids[i]))
  time.sleep(2) #if you want to risk with the script not working properly, you can make it faster here
  try:
    timepassed = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[4]/span[1]").text
    if "days" not in timepassed:
      if "mins" in timepassed and "hr" in timepassed:
        count += 1
        print("We found a ERC20 token transaction {}".format(timepassed))
        print("From wallet {}".format(ids[i]))
  except Exception as e:
    if "NoSuchElementException" in str(e):
      continue

print(" ")
print("Found {} wallets in {}! Shutting down!".format(count, int(time.time()-start)))
