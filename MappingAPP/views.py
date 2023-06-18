from django.shortcuts import render
from django.views.generic import TemplateView 

# Create your views here.


class map(TemplateView):
        template_name ="index.html"

class error(TemplateView):
        template_name ="404.html"
        
class about(TemplateView):
        template_name ="about.html"
        

        
class Allclients(TemplateView):
        template_name ="Allclients.html"
        
        

class BasicClient(TemplateView):
        template_name ="BasicClient.html"

class blackgray(TemplateView):
        template_name ="Black_Gray.html"
        
class Black_Grayclients(TemplateView):
        template_name ="Black_Grayclients.html"
        

        
class contact(TemplateView):
        template_name ="contact.html"
        
        
class Datamanagement(TemplateView):
        template_name ="Datamanagement.html"

class ecomClients(TemplateView):
        template_name ="ecomClients.html"
        
class feature(TemplateView):
        template_name ="feature.html"
        
class Goldclients(TemplateView):
        template_name ="Goldclients.html"
        
        


class Japanese(TemplateView):
        template_name ="Japanese.html"

class Japaneseclients(TemplateView):
        template_name ="Japaneseclients.html"
        
class login(TemplateView):
        template_name ="login.html"
        

        
class MappingClients(TemplateView):
        template_name ="MappingClients.html"
        
        

class Minimalist(TemplateView):
        template_name ="Minimalist.html"

class Minimalistclients(TemplateView):
        template_name ="Minimalistclients.html"
        
class Neo_Traditional(TemplateView):
        template_name ="Neo_Traditional.html"
        

        
class Neo_Traditionalclients(TemplateView):
        template_name ="Neo_Traditionalclients.html"
        
        
class Realism(TemplateView):
        template_name ="Realism.html"

class realismclients(TemplateView):
        template_name ="realismclients.html"
        
class service(TemplateView):
        template_name ="service.html"
        
class Signup(TemplateView):
        template_name ="Signup.html"
        
        
        
class SilverClients(TemplateView):
        template_name ="SilverClients.html"
        
        
class team(TemplateView):
        template_name ="team.html"

class testimonial(TemplateView):
        template_name ="testimonial.html"
        
class Traditional(TemplateView):
        template_name ="Traditional.html"
        
class Traditionalclients(TemplateView):
        template_name ="Traditionalclients.html"
        
        


class Watercolor(TemplateView):
            template_name ="Watercolor.html"
        
        
class Watercolorclients(TemplateView):
        template_name ="Watercolorclients.html"
