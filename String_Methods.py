#Your boss at the Poetry organization sent over a bunch of author names that he wants you to prepare for importing into the database. Using .split() and the provided string, create a list called author_names containing each individual author name as it’s own string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")

#Create another list called author_last_names that only contains the last names of the poets in the provided string.


author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

  #You’ve been provided with a list of words from the first line of Jean Toomer’s poem Reapers.Use .join() to combine these words into a sentence and save that sentence as the string reapers_line_one.


reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)



#You’ve been given a list, winter_trees_lines, that contains all the lines to William Carlos Williams poem, Winter Trees. You’ve been asked to join together the strings in the list together into a single string that can be used to display the full poem. Name this string winter_trees_full.

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)



#Use .strip() on each line in the list below to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for lines in love_maybe_lines:
    love_maybe_lines_stripped.append(lines.strip())

#.join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.Each line of the poem should show up on its own line.
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

#Print love_maybe_full.
print(love_maybe_full)


#Use .replace() to change all instances of Tomer in the bio to Toomer. Save the updated bio to the string toomer_bio_fixed.

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

#At what index place does the word “disown” appear? Save that index place to the variable disown_placement.

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")

#Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The function should use .format() to return the following string: The poem "[TITLE]" is written by [POET].Remember to escape the " characters using \".

def poem_title_card(title, poet):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc

print(poem_title_card("I Hear America Singing","Walt Whitman"))


#The function poem_description is supposed to use .format() to print out some quick information about a poem, but it seems to be causing some errors currently.Fix the function by using keywords in the .format() method.

def poem_description(publishing_date, author, title, original_work):
 return "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
 
my_beard_description = poem_description("1974", "Shel Silverstein","My Beard","Where the Sidewalk Ends")


