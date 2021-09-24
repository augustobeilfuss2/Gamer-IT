"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from app.models import Players, Cursos
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from app.forms import InserePlayerForm, InsereCursosForm
from django.urls import reverse_lazy
from decimal import Decimal, getcontext

class IndexTemplateView(TemplateView):
    template_name = "app/index.html"


#Players

class ListaPlayers(ListView):
    template_name = "app/Players.html"
    model = Players
    context_object_name = "Players"

def post_createPlayer(request):
    
    form = InserePlayerForm()
    if(request.method == 'POST'):
        form = InserePlayerForm(request.POST)
        if(form.is_valid()):

            
            post_nmColaborador = form.cleaned_data['nmcolaborador']
            post_imColaborador = form.cleaned_data['imcolaborador']
            post_nmSetor = form.cleaned_data['nmSetor']

            new_post = Players(nmcolaborador = post_nmColaborador,imcolaborador=post_imColaborador, nmSetor = post_nmSetor )
            new_post.save()
            return redirect('app:lista_player')
    elif(request.method == 'GET'):
        return render(request, 'app/player_form.html', {'form': form})

class PlayerUpdate(UpdateView):
    template_name = "app/player_update.html"
    model = Players
    fields = [
      'nmcolaborador',
      'imcolaborador' ,
      'nmSetor',
      
    ]  

    def form_valid(self, form):
       
        form.instance.nmcolaborador = form.instance.nmcolaborador
        form.instance.imcolaborador = form.instance.imcolaborador
        form.instance.nmSetor = form.instance.nmSetor
        #self.object = form.save()

        

        

        #id = form.instance.pk
        #print(id)
        #id.save()
        #subtotal = Players.objects.filter(id=id)
        
        #id.save()
        #form=Players(nmcolaborador = post_nmcolaborador, imcolaborador=post_imcolaborador, nmSetor= post_nmSetor, id=2)
        #print(form)
      
        redirect_url = super(PlayerUpdate, self).form_valid(form)

        return redirect_url


    context_object_name = 'players'
    success_url = reverse_lazy("app:lista_player")
    

class PlayerDelete(DeleteView):
    template_name = "app/player_delete.html"
    model = Players
    context_object_name = 'players'
    success_url = reverse_lazy("app:lista_player")




#Cursos

class ListaCursos(ListView):
    template_name = "app/Cursos.html"
    model = Cursos
    context_object_name = "Cursos"

def post_create(request):
    
    form = InsereCursosForm()
    if(request.method == 'POST'):
        form = InsereCursosForm(request.POST)
        print(form)

        if(form.is_valid()):

            def calculos():
                post_nmCurso = form.cleaned_data['nmCurso']
                post_acFaculdade = form.cleaned_data['acFaculdade']
                post_nuMaterias = form.cleaned_data['nuMaterias']
                post_nmInstituicao = form.cleaned_data['nmInstituicao']
                post_nmPlayer = form.cleaned_data['nmPlayer']
                post_nuHoras = form.cleaned_data['nuHoras']
                post_acWorkshop = form.cleaned_data['acWorkshop']
                post_acImplementacao = form.cleaned_data['acImplementacao']
                post_acComunik = form.cleaned_data['acComunik']

                def seFaculdade(post_acFaculdade, post_nuMaterias, post_nuHoras):
                    if post_acFaculdade == True:
                        post_nuHoras = post_nuMaterias * 4
                        return post_nuHoras             
                    else:
                        return post_nuHoras

                post_nuHoras = seFaculdade(post_acFaculdade, post_nuMaterias, post_nuHoras)
                
                def ptWorkshopsF(post_nuHoras, post_acWorkshop):
                    if post_acWorkshop == True:
                        v = post_nuHoras * 0.2
                        return v
                    else:
                        return 0

                def ptImplementacaoF(post_nuHoras, post_acImplementacao):
                    if post_acImplementacao == True:
                        return post_nuHoras * 0.45
                    else:
                        return 0

                def ptComunikF(post_nuHoras, post_acComunik):
                    if post_acComunik == True:
                        return post_nuHoras * 0.1
                    else:
                        return 0
            
                getcontext().prec=2

                post_ptHoras = round(post_nuHoras * 0.45,2)
                post_ptWorkshop = round(ptWorkshopsF(post_nuHoras, post_acWorkshop),2)
                post_ptImplementacao = round(ptImplementacaoF(post_nuHoras, post_acImplementacao),2)
                post_ptComunik = round(ptComunikF(post_nuHoras, post_acComunik),2)

                

                new_post = Cursos(nmCurso=post_nmCurso, acFaculdade=post_acFaculdade, nuMaterias=post_nuMaterias,nmInstituicao=post_nmInstituicao, nmPlayer=post_nmPlayer,nuHoras=post_nuHoras, ptHoras=post_ptHoras,acWorkshop = post_acWorkshop, ptWorkshop=post_ptWorkshop ,acImplementacao= post_acImplementacao, ptImplementacao=post_ptImplementacao,acComunik = post_acComunik, ptComunik=post_ptComunik)
                print(new_post)
                new_post.save()
            calculos()   
            return redirect('app:lista_curso')
    elif(request.method == 'GET'):
        return render(request, 'app/curso_forms.html', {'form': form})

def post_update(request, pk):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaa" + pk)  
    print("bbbbbbbbbbbb")
    form = InsereCursosForm()
    if(request.method == 'POST'):
        form = InsereCursosForm(request.POST)
        print(form)

        if(form.is_valid()):

            
            post_nmCurso = form.cleaned_data['nmCurso']
            post_acFaculdade = form.cleaned_data['acFaculdade']
            post_nuMaterias = form.cleaned_data['nuMaterias']
            post_nmInstituicao = form.cleaned_data['nmInstituicao']
            post_nmPlayer = form.cleaned_data['nmPlayer']
            post_nuHoras = form.cleaned_data['nuHoras']
            post_acWorkshop = form.cleaned_data['acWorkshop']
            post_acImplementacao = form.cleaned_data['acImplementacao']
            post_acComunik = form.cleaned_data['acComunik']

            def seFaculdade(post_acFaculdade, post_nuMaterias, post_nuHoras):
                if post_acFaculdade == True:
                    post_nuHoras = post_nuMaterias * 4
                    return post_nuHoras             
                else:
                    return post_nuHoras

            post_nuHoras = seFaculdade(post_acFaculdade, post_nuMaterias, post_nuHoras)

            def ptWorkshopsF(post_nuHoras, post_acWorkshop):
                if post_acWorkshop == True:
                    v = post_nuHoras * Decimal('0.2')
                    return v
                else:
                    return 0

            def ptImplementacaoF(post_nuHoras, post_acImplementacao):
                if post_acImplementacao == True:
                    return post_nuHoras * Decimal('0.45')
                else:
                    return 0

            def ptComunikF(post_nuHoras, post_acComunik):
                if post_acComunik == True:
                    return post_nuHoras * Decimal('0.1')
                else:
                    return 0
            
            getcontext().prec=2

            post_ptHoras = float((Decimal(post_nuHoras * 0.45))/Decimal('1')) 
            post_ptWorkshop = float(Decimal(ptWorkshopsF(post_nuHoras, post_acWorkshop))/Decimal('1')) 
            post_ptImplementacao = float(Decimal(ptImplementacaoF(post_nuHoras, post_acImplementacao))/Decimal('1')) 
            post_ptComunik = float(Decimal(ptComunikF(post_nuHoras, post_acComunik))/Decimal('1'))

            new_post = Cursos(nmCurso=post_nmCurso, acFaculdade=post_acFaculdade, nuMaterias=post_nuMaterias,nmInstituicao=post_nmInstituicao, nmPlayer=post_nmPlayer,nuHoras=post_nuHoras, ptHoras=post_ptHoras,acWorkshop = post_acWorkshop, ptWorkshop=post_ptWorkshop ,acImplementacao= post_acImplementacao, ptImplementacao=post_ptImplementacao,acComunik = post_acComunik, ptComunik=post_ptComunik)
            print(new_post)
            new_post.save()
            return redirect('app:lista_curso')
    elif(request.method == 'GET'):
        return render(request, 'app/curso_update.html', {'form': form})


def update(request, pk):
   form= InsereCursosForm()
   if(request.method == 'POST'):
        form = InsereCursosForm(request.POST)
        print(form.cleaned_data['nuHoras'])
        print(request)
        print("aaa" + pk)
        print(id)
        print(form)
        print(pk.nuHoras)
        form.nmCurso = request.POST.get('nmCurso')
        print(form.nmCurso)
        #cursos = Cursos.objects.get(pk=Cursos.id)
        #you can do this for as many fields as you like
        #here I asume you had a form with input like <input type="text" name="name"/>
        #so it's basically like that for all form fields
        #update_post=Cursos(nmCurso=post_nmCurso, acFaculdade=post_acFaculdade, nuMaterias=post_nuMaterias,nmInstituicao=post_nmInstituicao, nmPlayer=post_nmPlayer,nuHoras=post_nuHoras, ptHoras=post_ptHoras,acWorkshop = post_acWorkshop, ptWorkshop=post_ptWorkshop ,acImplementacao= post_acImplementacao, ptImplementacao=post_ptImplementacao,acComunik = post_acComunik, ptComunik=post_ptComunik)
        #form.save()
        #print(cursos)
   
        return HttpResponse('updated')
   elif(request.method == 'GET'):
        
        
        
        return render(request, 'app/curso_update.html', {'form': form})
  

class CursosUpdate(UpdateView):
    template_name = "app/curso_update.html"
    model = Cursos
    fields = [
        'nmCurso',
        'acFaculdade',
        'nuMaterias',
        'nmInstituicao',
        'nmPlayer',
        'nuHoras',
        'acWorkshop',
        'ptWorkshop',
        'acImplementacao',
        'ptImplementacao',
        'acComunik',
        'ptComunik',
      
    ]

    context_object_name = 'cursos'
    success_url = reverse_lazy("app:lista_curso")

    def form_valid(self, form):

        
        def ptWorkshopsF(post_nuHoras, post_acWorkshop):
                    if post_acWorkshop == True:
                        v = post_nuHoras * 0.2
                        return v
                    else:
                        return 0

        def ptImplementacaoF(post_nuHoras, post_acImplementacao):
                    if post_acImplementacao == True:
                        return post_nuHoras * 0.45
                    else:
                        return 0

        def ptComunikF(post_nuHoras, post_acComunik):
                    if post_acComunik == True:
                        return post_nuHoras * 0.1
                    else:
                        return 0

        def seFaculdade(post_acFaculdade, post_nuMaterias, post_nuHoras):
                    if post_acFaculdade == True:
                        post_nuHoras = post_nuMaterias * 4
                        return post_nuHoras             
                    else:
                        return post_nuHoras

        form.instance.nuHoras = seFaculdade(form.instance.acFaculdade, form.instance.nuMaterias, form.instance.ptHoras)


        getcontext().prec=2
        
        form.instance.ptHoras = round(form.instance.nuHoras * 0.45,2)
        form.instance.ptWorkshop = round((ptWorkshopsF(form.instance.nuHoras, form.instance.acWorkshop)),2)
        form.instance.ptImplementacao = round((ptImplementacaoF(form.instance.nuHoras, form.instance.acImplementacao)),2)
        form.instance.ptComunik = round((ptComunikF(form.instance.nuHoras, form.instance.acComunik)),2)
        
        
        
        #form.instance.net = form.instance.qty * form.instance.price
        #redirect_url = super(OrderDetailsProductEdit, self).form_valid(form)
        #order = Order.objects.get(pk=self.kwargs['order_id'])
        #subtotal = OrdersPlaced.objects.filter(order=order).aggregate(Sum('net'))['net__sum']
        #order.subtotal = subtotal
        #order.save()

        redirect_url = super(CursosUpdate, self).form_valid(form)
        return redirect_url

class CursoDelete(DeleteView):
    template_name = "app/curso_delete.html"
    model = Cursos
    context_object_name = 'cursos'
    success_url = reverse_lazy("app:lista_curso")




#V1 apagar

class PlayerCreateView(CreateView):
    template_name = "app/player_form.html"
    model = Players
    form_class = InserePlayerForm
    success_url = reverse_lazy("app:lista_player")

class CursosCreateView(CreateView):
    template_name = "app/curso_form.html"
    model = Cursos
    form_class = InsereCursosForm
    success_url = reverse_lazy("app:lista_curso")


   
