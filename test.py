# import the 
from simple_nlp_mmg.simple_nlp import simple_nlp

#-------------------------------------------------------------------------
# Importing Text
#-------------------------------------------------------------------------
text = u'fish carp whale, shark, dog,]] wolf cat lion tiger. There was once a little boy named Ben, that liked to play with fire. His mother told him that fire was dangerous, so he decided that he would buy a box of matches and head to the lake. As an extra precaution, he swam to the bottom of the lake and lit a fire. There he met a fish who has cold and sat beside him at the bottom of the lake. The fish asked the boy "how did you light a fire underwater?" to which the boy responded "How would a fish know what fire looks like?". "The stars are on fire" said the fish, "and from my home in the lake, I can see the stars at night". "Now how would you know that stars are on fire?" said the boy. "In the same way that you know I am fish" relplied the fish.' 
snlp = simple_nlp(text)

#-------------------------------------------------------------------------
# Preprocess the text
#-------------------------------------------------------------------------
snlp.preprocess(stoplist=[])
print(snlp.clean_text)
print(snlp.sentence_num)
print(snlp.tokens)
print(snlp.tags)
print(snlp.entity)


