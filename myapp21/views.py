from django.template import RequestContext
from django.shortcuts import render_to_response

# creating a function
# creating request context--->for server to remember where the req came from
# passing local variables
# return statement
def home(request):
	ctx=RequestContext(request)
	temp_name="index.html"
	mylocals={}
	return render_to_response(temp_name,mylocals,ctx)

def about(request):
	ctx=RequestContext(request)
	temp_name="about.html"
	mylocals={}
	return render_to_response(temp_name,mylocals,ctx)
