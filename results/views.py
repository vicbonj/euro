from django.shortcuts import render, get_object_or_404
from results.models import Pointing
from .forms import JoinForm, PointingForm
import os
import numpy as np
import time
from django.http import HttpResponse
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import FormView
from django.http import JsonResponse

class JoinFormView(FormView):
    form_class = JoinForm
    template_name = 'results/query.html'
    success_url = '/'
    
    def form_invalid(self, form):
        response = super(JoinFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView, self).form_valid(form)
        if self.request.is_ajax():
            time.sleep(1.5)
            jah = form.cleaned_data
            numb_grille = int(jah['n_grilles'])

            numeros = []
            for i in range(numb_grille):
                nums_1 = np.random.choice(np.arange(50)+1, 5, replace=False)
                nums_2 = np.random.choice(np.arange(12)+1, 2, replace=False)
                nums_1.sort()
                nums_2.sort()
                nums_1 = ' '.join(str(num).zfill(2) for num in nums_1)
                nums_2 = ' '.join(str(num).zfill(2) for num in nums_2)
                nums = [nums_1, nums_2]
                numeros.append(' - '.join(str(num) for num in list(nums)))

            data = {'nums': '<br>'.join(numeros)}

            return JsonResponse(data)
        else:
            return response
