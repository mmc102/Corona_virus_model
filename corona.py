#read an article about spread of the desease and figured it would be fun to try to model it myself
import random
 

#now one person has the corona virus.  lets make a variable for now many people interact with each other 
#https://medium.com/@jaylin/how-many-people-do-you-think-you-interact-with-on-your-average-day-d15bed024f6c  tldr: 25. seems reasonable enough on average 
#so everyone in the population sees 25 other members of the population 
num_of_interactions = 5
#https://www.medicalnewstoday.com/articles/coronavirus-may-spread-faster-than-who-estimate#Higher-estimates-than-WHO-predict
#each infection likely passes to 2.79 people
transmission_rate = 2.79/num_of_interactions #~11% chance of transmission upon a given interaction 
death_rate = 1/100
#make interactions 
#does it matter if numbers are selected in clusters? or does radomized interactions matter?
#to make countries i can make bins, have alot of interaction in the bins, then have small interaction numbers bin to bin 




def cycle_of_interaction(num_interactions, rate_trans, num_cycles,death_rate,travel_frequency):    
    cycles = 0 
    death_count = 0 
    num_sick = 0
    #initiate a list within a list 
    population = []
    citizens = 70000
    person_number = 1
    while len(population) < citizens:
        
        #[person ID,alive(1)/dead(0), infection y/n (1,0)
        population.append([person_number,1,0]) 
        person_number+=1
        
    #infect a random person
    
    population[random.randrange(citizens)][2] = 1 

    num_of_bins = citizens/50 #make 50 person bins
    the_bins = []  #each bin contains 50 people which are a list of atributes 
    while len(the_bins) < num_of_bins:
        the_bins.append([])

    #add people to the bins 'countries' 
    bin_assignment = 0
    while bin_assignment < num_of_bins:
        bin_fill_level = 1
        for i in population:
            the_bins[bin_assignment].append(i)
            if bin_fill_level == (citizens/num_of_bins):
                bin_assignment +=1
                bin_fill_level = 0
            bin_fill_level +=1

    while cycles < num_cycles:
        for country in the_bins: #"county level"
            for person in country: #person level
                #each person needs to interact with x other people in the same list.  when they make the encounter, we do math to determine if they indeed get the virus 
                interactions_this_cycle = 0
                while interactions_this_cycle < num_interactions:
                    if country[random.randrange(len(country))][2] == 1: #basically if they meet someone infected  
                        pass_disease = random.randrange(1000) #generate num between 1-100, 8% chance of transmission, so if num < 8, they get the virus
                        if pass_disease < 1000*rate_trans:
                            person[2] = 1
                    
                    interactions_this_cycle +=1                            
            
            if cycles % travel_frequency == 0:  ## if travel frequency is 3 per say, every 3 days someone will interact with someone outside their country 
                if the_bins[random.randrange(len(the_bins))][random.randrange(len(the_bins[0]))][2] == 1:  ##if the random person travels without it, no action
                    pass_disease = random.randrange(1000) #if they are sick, generate num between 1-100, 8% chance of transmission, so if num < 8, they get the virus
                    if pass_disease < 1000*rate_trans:  #if they do pass the disease
                        the_bins[random.randrange(len(the_bins))][random.randrange(len(the_bins[0]))][2] = 1    #pick random person and give them the disease 
        bin_no = 0
        
        for i in the_bins:
            num_sick = num_sick + (sum(j[2] for j in i))
        #print(num_sick, 'out of', citizens)
                        

        cycles += 1
        
    return num_sick

trials = 0
results = [] 
while trials < 20:
    results.append(cycle_of_interaction( num_of_interactions,transmission_rate,15,death_rate,3))
    trials+=1
    print(trials)
print('average', sum(results)/len(results))


