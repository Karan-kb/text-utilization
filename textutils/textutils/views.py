# I create this file. -Karan


from django.http import HttpResponse

from django.shortcuts import render
def index(request):


    return render(request, 'index.html')


def ex1(request):


    s ='''<h1>Navigation Bar <br> </h1>
    <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">Harry Code</a>
    <br<
    <a href="https://www.facebook.com/">Facebook</a><br>
    <a href="https://www.edfenergy.com/">EDF</a><br>
    <a href="https://www.instagram.com/">Instagram</a><br>
    <a href="https://www.instagram.com/">Instagram</a> '''
    
    return HttpResponse(s)
    


def about(request):
    return HttpResponse('''<a href="https://www.facebook.com/">Karan<a>''')


def analyze(request):
    nav = '''
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
        </ul>
    </nav>
    '''
    #get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount= request.GET.get('charcount', 'off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    if removepunc == "on":


        punctuations = '''.,.( )…( )[ ]“ ”!?–—;,'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed=""

        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to UPPERCASE', 'analyzed_text': analyzed}
            # analyze the text
        return render(request, 'analyze.html', params)



    elif(extraspaceremover == "on"):
        analyzed = ""

        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]== " "):

                analyzed = analyzed + char
        params = {'purpose': 'Remove Spaces.', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    elif (charcount == "on"):
        analyzed = ""

        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'Count Charcters', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)


    elif (newlineremover == "on"):
        analyzed = ""

        for char in djtext:
            if char != '\n':  # Check if the character is not a newline
                analyzed += char

        params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)



    else:
        return HttpResponse("Error")


# def capfirst(request):
#
#     return HttpResponse("Capitalize First")
#
# def newlineremove(request):
#     return HttpResponse("New Line Remove")
#
# def spaceremove(request):
#     return HttpResponse('Space Remove')
# def charcount(request):
#     return HttpResponse('Character Count')


# def index(request):
#     nav = '''
#
#             <h1>Home</h1>
#
#              <li><a href="removepunc">Remove Punctuation</a></li>
#              <li><a href="capitalizefirst">Capitalization</a></li>
#              <li><a href="newlineremove">New Line Remover</a></li>
#              <li><a href="spaceremove">Space Remover</a></li>
#              <li><a href="charcount">Charecter Counter</a></li>
#             '''
#     return HttpResponse(nav)

