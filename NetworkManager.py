class NetworkManager:
    def __init__(self):
        self.transactions = []

    def read_file(self):
        with open("apache_access.bib", "r") as file:
            for line in file: 
                elements = line.split(" ")
                transaction = {
                    'ip' : elements[0],
                    'timestamp' : "".join([elements[3].strip("[]"),elements[4].strip("[]")]),
                    'kind_of_petition' : elements[5],
                    'route' : elements[6],
                    'version' : elements[7].strip('"'),
                    'status' : elements[8],
                    'completed_time': elements[9].strip('\n')
                }
                self.transactions.append(transaction)
            
    
    def detect_ip(self): 
        ips = {}
        for transaction in self.transactions: 
            if transaction['ip'] in ips:
                ips[transaction['ip']] += 1
            else: 
                ips[transaction['ip']] = 1
            
        max_value = max(ips.values())
        ip_of_max_value = [key for key, val in ips.items() if val == max_value][0]
        
        num_of_petitions = 0
        banned_ips = {}
        for transaction in self.transactions:                 
            if transaction['ip'] in banned_ips: 
                print(transaction['ip'], "HEY YOU'RE BANNED 👺")

            #Get the timelapse 
            time

            #Compare the timelapse and secure that the num_of_petitions is not equal to 15
            
            if transaction['ip'] == ip_of_max_value:
                if num_of_petitions == 15:
                    banned_ips[ip_of_max_value] = 1
                    num_of_petitions = 0  
                else:
                    num_of_petitions += 1

        print(banned_ips)
        print(self.transactions)
                
        """
            IF THE IP MAKES A REQUEST IN A TIMELAPSE OF LEST THAN 3S
                IF THE AMOUNT OF REQUEST IS GREATER THAN 15
                    ADD THE IP TO THE BANNED IPS DICT

            KEEP TRAVERSING OUR DICT AND LOOK UP AT THE BANNED IPS
                IF A BANNED IP APPEARS SEND A MESSAGE THAT SAYS "HEY YOU'RE BANNED 👺" 
        """
        