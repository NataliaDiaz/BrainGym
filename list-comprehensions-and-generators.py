# Assuming a very long list of elements, how to apply certain parsing operation to each of them?
list_of_messages = ['..', '...']
def parser(input):
    return "*"



# Initial solution: given that we have defined parser(), a lambda function here is no more efficient than the following:
parsed_list = []
for element in list_of_messages:
    parsed_list.append(parser(element))

print parsed_list

# How to make it shorter and more efficient?
parsed_list = [parser(element) for element in list_of_messages]

# What if we do not need a parsed_list in memory, just one parsed element at a time?
def get_parsed_element(list_of_messages, x):
    return parsed(list_of_messages[x])

# Now we are receiving list_of_messages one by one as a stream of input
# generator_of_messages = generator
# What is an efficient way to not having to compute and have in memory such million elements computed,
# if we will just need some of them and can compute in the fly? we use list comprehension (more efficient than the former)

d = {
    1: 2,
    3: 4,
    5: 6
}

# How to make it more efficient and shorter? With list comprehensions:
for key, value in d.iteritems():
    print key, value


# How to make it even faster? paralellizing each operation in a cluster,
# since each process is independent on the previous data operation: map reduce, hadoop, etc

"""
Design front and back end so the whole company organization can access every employee and all the company's info easily.
the KB easily and pose questions anytime without difficulty and without having to see any deep learning under the hood.
----
PROPOSAL:

DATA acquisition:
    Social media from our Fb page and twitter account, Linkedin and Customer support email.
    News data, forums, online debate, etc.

    Conversational model input:
        Questions and answers: email2QA algorithm

bABI/Quora dataset for Q&A
Initial clustering / t-SNE visualization to name the questions topics
LDA to find the topic

KB: questions and answers and context (topic model label)


Backend:
    1. Relational Database: MySQL DB
-------
Departments, Employees, Customers, Partners, Investors
Transactions, Contracts
-------
    2. NoSQL Database (ontological DB):
        RDF/ Lucene/ Elastic search
           |
        Flask application /NodeJS/Django/React
           |
        GUI
           |
        Q & A


Example of input data:
msg = "Hi how are you, I'm very interested, please point me int he direction of your pricing page"

Under the hood:
answer = kb(msg)

poser = find (email, poser)
role = find(poser, 'role')

sentiment = get_sentiment(msg)
grounding = sentence without article and pronouns.
groundting triples = triplification(grounding) // Triplify, r2rdf, (any NL2RDF service),
RDF: (subject, predicate, object)
result = SPARQL(grounding triples)

SPARQL;
select answer
where request = grounding triples: (companyX, hasPricingWebPage, x?)

"""
