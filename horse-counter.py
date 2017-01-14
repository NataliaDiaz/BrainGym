"""
Horse counter
There are a lot of horses in the yard, and we want to count how many there are.
Unfortunately, we've only got a recording of the sounds from the yard.
All the horses say "neigh".  The problem is they can "neigh" many times.
The recording from the yard is sadly all mixed together.  So, we need to figure
out from the overlapping sounds how many horses there could be.

For example, we've got two horses in the yard, and we hear this "neigneighh".
From this recording, we can successfully deduce there are 2 horses.  Another
example is "neighneigh".  From this example, we can only tell there is one horse
in the yard.

As an additional complexity, our recording might not be perfect.  If it's a bad
recording, we should give "Invalid" as the response.

The input will be given as a string on one line.  The output should be printed
on it's own line.

Sample Input
nenigehnieighgh

Sample Output
2
"""


# This is Python 2
import sys

NEIGH = 'neigh'

def remove_neigh_s(sound):
    return sound.replace(NEIGH, '')

def is_valid_sound(sound):
    if remove_neigh_s(sound) == '':
        return True
    elif len(set(list(sound))) != len(NEIGH):
        # if extra charaters
        return False
    else:
        return True
        #overlap1, overlap2 =
        # print sound.split(NEIGH)
        # print "splitting by neigh: ", overlap1, overlap2
        # if is_valid_sound(overlap1) and is_valid_sound(overlap2):
        #     return True
        # else:
        #     if is_valid_sound(overlap2) and not is_valid_sound(overlap1) and fits_in_barn(overlap1):
        #         return True
        #     elif is_valid_sound(overlap1) and not is_valid_sound(overlap2) and fits_in_barn(overlap2):
        #         return True
        #     else:
        #         return False

def follows(current_sound, phoneme):
    template = 'neigh'
    phoneme_pair = current_sound[-1]+ phoneme
    print "follows ", phoneme_pair
    if phoneme_pair in template:
        return True
    else:
        return False

def add_to_sound(barn, phoneme):
    if phoneme in 'neigh':
        if len(barn)>0:
            for sound in range(len(barn)):
                if follows(phoneme, barn[sound][-1]):
                    barn[sound] = (barn[sound]+phoneme)
                    print "Phoneme added to sound: state of barn: ", barn
                    return barn
                elif phoneme == 'n':
                    # new horse
                    barn.append('n')
                    return barn
        else:
            barn.append('n')
            return barn
        print "Phoneme could not be added to sound: ", barn, " Invalid"
        return "add_to_sound Invalid input!"
    else:
        return "add_to_sound Invalid input!"
# if len(line)>=len(NEIGH):
#     current_sound = line[0]
#     line = line[1:]
#     while len(line) >=2:
#         phoneme = line[0]
#         if belongs_to_current_sound(current_sound, phoneme):
#             if phoneme == 'h':
#                 horses += 1
#         else:
#             barn = add_to_sound(barn, phoneme)
#
#         phoneme = line[0]
#         line = line[1:]
# print horses

def count_horses(line):
    print "\n\n++++++++++++++++++++++++ Counting horses for sound: ",line, " ++++"
    # keep list of stacks to keep track of horses singing at the same time
    barn = []
    line = str(line).strip()
    if not is_valid_sound(line):
        print "Invalid "
        return
    else:
        horses = line.count(NEIGH)
        # Remove uninterrumpted horses first to find the noise of overlapping ones later
        print horses," uninterrumpted horses"
        if horses>1:
            horses = 1 # no guarantee there is more than one
        line = remove_neigh_s(line)

        # after removing parallel potential noise, we can keep removing complete NEIGH and Counting
        # until we have taken all the words out from the sound. If the end results in "" sound, it is valid
        while len(line) >= len(NEIGH):
            n_horses = line.count(NEIGH)
            horses += n_horses
            line = remove_neigh_s(line)
            if n_horses ==0:
                break
        if line != '':
            print "Invalid"
            return
        print horses
        return horses

# line = sys.stdin.readline()
# print line
# count_horses(line)
count_horses("nenigehnieighgh")
count_horses("neighneighneigh")
count_horses("neighnneigheigh")
count_horses("nnneneighigh")
count_horses("neighnnneigheineighgheineighgh") #neigh n n neigh ei neigh gh ei neigh gh")
