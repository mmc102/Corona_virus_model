#read an article about spread of the desease and figured it would be fun to try to model it myself

#initiate a list within a list 
population = []
citizens = 700
person_number = 1
while len(population) < citizens:
    
    #[person ID,alive(1)/dead(0), infection y/n (1,0)
    population.append([person_number,1,0]) 
    person_number+=1
    
#infect a random person
import random
population[random.randrange(citizens)][2] = 1  

#now one person has the corona virus.  lets make a variable for now many people interact with each other 
#https://medium.com/@jaylin/how-many-people-do-you-think-you-interact-with-on-your-average-day-d15bed024f6c  tldr: 25. seems reasonable enough on average 
#so everyone in the population sees 25 other members of the population 
num_of_interactions = 25
#https://www.medicalnewstoday.com/articles/coronavirus-may-spread-faster-than-who-estimate#Higher-estimates-than-WHO-predict
#each infection likely passes to 2.79 people
transmission_rate = 2.79/num_of_interactions #~11% chance of transmission upon a given interaction 
death_rate = 3/100
#make interactions 
#does it matter if numbers are selected in clusters? or does radomized interactions matter?
#to make countries i can make bins, have alot of interaction in the bins, then have small interaction numbers bin to bin 
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


def cycle_of_interaction(the_bins,num_interactions, rate_trans, num_cycles,death_rate):    
    cycles = 0 
    death_count = 0 
    while cycles < num_cycles:
        for country in the_bins: #"county level"
            for person in country: #person level
                #each person needs to interact with x other people in the same list.  when they make the encounter, we do math to determine if they indeed get the virus 
                interactions_this_cycle = 0
                while interactions_this_cycle < num_interactions:
                    if country[random.randrange(len(country))][2] == 1: #basically if they meet someone infected  
                        pass_disease = random.randrange(100) #generate num between 1-100, 8% chance of transmission, so if num < 8, they get the virus
                        if pass_disease < 100*rate_trans:
                            person[2] = 1
                            death = random.randrange(100)
                            
                            if death < death_rate:
                                person[1] = 0
                                death_count +=1
                                print("DEATH COUNT:", death_count)
                                print('CYCLE NUMBER:', cycles)
                                
                    interactions_this_cycle +=1
        cycles += 1
cycle_of_interaction(the_bins, num_of_interactions,transmission_rate,100,death_rate)

    