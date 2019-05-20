from string import Template
"""
Import the “Template” class from the standard library’s “string”
module. This allows for simple string-substitution templates.
"""



def start_response(resp="text/html"):
    return('Content-type:'+ resp +'\n\n')
""" this function takes a single optional string as it's argument and uses it to create a cgi content type line,
with text/html as the default
"""




def include_header(the_title):
    with open("header.html") as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
"""
open the template for an html header. 
creates the title of the page. the page itself is stored within a separate file in "template/header.html
"""



def include_footer(the_links):
    with open("footer.html") as footf:
        foot_text = footf.read()
    link_string = ""
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key +\
                            '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return (footer.substitute(links=link_string))
"""
the footer text of the page. the argument is used to dynamically create a set of HTML link tags. 
 
"""





def start_form(the_url, form_type="POST"):
    return('<form action ="' + the_url + '"method='+form_type+ '">')
"""
method to get the url of our webpage. (returns the html for the start of a form and lets the called spcify url)
"""



def end_form(submit_msg="Submit"):
    return ('<p></p>input type =submit value="' + submit_msg + '"></form')
"""
terminates the form , an allows customisation of submit button 
"""



def radio_button(rb_name, rb_value):
    return('<input type="radio" name="'+rb_name+\
           '"value="'+ rb_value + '">' + rb_value + '<br/>')
"""

given a ratop-button name and value, create a html radio button.
"""



def u_list(items):
    u_string='<ul>'
    for item in items:
        u_string += '<li>' + item +'</li>'
    u_string += '</ul>'
    return (u_string)
"""
list of items in this case athletes/times . and turn them into a html unnerber list.
"""



def header(header_text, header_level=2):
 return('<h' + str(header_level) + '>' + header_text +
 '</h' + str(header_level) + '>')

"""
Create and return a HTML header tag (H1, H2, H2, and so on) with level 2
as the default.. The “header_text” argument is required.
"""




def para(para_text):
 return('<p>' + para_text + '</p>')
"""
Enclose a paragraph of text (a string) in HTML paragraph tags. Almost not
worth the effort, is it?
"""


print(start_response())
print(start_response("text/plain"))
print(start_response("application/json"))

print(include_header("Good Day!"))


"""
The include_footer() function produces HTML that terminates a web page, providing links (if provided as a
dictionary). An empty dictionary switches off the inclusion of the linking HTML:
"""
print(include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'})) # with link included
print(include_footer({})) # without link


print(start_form("athlete_List.py"))

print(end_form())

print(end_form("Click to confirm Your Order"))


"""
The start_form() and end_form() functions bookend a HTML form, with the parameter (if supplied)
adjusting the contents of the generated HTML:
"""
for i in ["John","Paul","George","Ringo"]:
    print(radio_button(i,i))


"""
Unordered- lists 
"""
print(u_list(["Life of Brian",'Holy Grail']))

"""
The header() function lets you quickly format HTML headings at a selected level (with 2 as the default):
"""
print(header("welcome!"))

print(header("welcome again!", 5 ))   # selected level


"""
encloses chunk of text within HTML paragraphs tags 
"""

print(para("what did it cost? Everything"))