from django.shortcuts import render

about_blog = {
    'content': '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ac ipsum orci. Vestibulum tempor neque libero, vitae hendrerit nulla ultricies ut. Cras vulputate, dui vitae pellentesque venenatis, lectus lacus ultricies odio, sed pharetra arcu diam in mauris. Morbi eget nibh egestas, tincidunt nisi vitae, tristique mauris. Nulla eget nisi in lorem varius pellentesque. Morbi at aliquet odio, ut efficitur ligula. Integer nec fermentum risus. Fusce felis arcu, convallis quis ligula vel, dignissim porttitor lectus.

Nulla placerat gravida consectetur. Etiam quis luctus nisi, eu laoreet neque. Proin tortor quam, lacinia id fermentum quis, scelerisque in mauris. Proin vestibulum ipsum volutpat orci bibendum ornare. In a consectetur tellus, sit amet lacinia ipsum. Praesent convallis nibh ut mauris tincidunt ultricies. Praesent ex risus, facilisis sed feugiat sed, tristique eget tellus. Nam in ante et risus rutrum dignissim eu lacinia nibh. Mauris in risus at nisl consectetur egestas. Maecenas varius pulvinar ligula, a fermentum urna luctus id.

Sed condimentum rhoncus lectus, id euismod odio posuere non. Maecenas a risus ac tortor finibus condimentum a quis ipsum. Morbi fringilla eleifend libero, vitae sagittis erat tincidunt in. Donec quis ipsum at lectus consectetur euismod. Etiam nec diam dapibus, elementum lacus eget, lacinia erat. Mauris ac tortor venenatis, egestas purus quis, suscipit justo. Aliquam molestie ut odio vel eleifend. Etiam tristique ac enim et tempus. Donec tincidunt viverra vehicula. Nulla semper convallis eleifend. Nam convallis erat turpis, dictum sagittis velit vehicula et. Sed ut arcu vitae lacus tristique accumsan. Duis consectetur metus at erat gravida bibendum. Donec blandit sit amet lorem ac ultrices. Nullam a eleifend magna. Phasellus in quam eros.

Morbi id orci blandit lacus interdum consequat dapibus in augue. Ut vel sodales nunc. Vestibulum mattis dictum orci eget laoreet. Nulla aliquet fringilla ligula, sit amet egestas metus dapibus et. Nam ligula purus, volutpat a efficitur at, molestie nec dui. In commodo ipsum eu dui iaculis mollis. Sed quis facilisis mi. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus hendrerit laoreet lorem sed bibendum. Morbi pulvinar augue mi, a tristique dolor sollicitudin non. Nam varius dignissim mauris, non varius orci semper sit amet. Praesent hendrerit mollis scelerisque. Duis vestibulum massa in magna lacinia, at volutpat justo eleifend. Sed eu lorem vel mi luctus tincidunt a non tortor.

Duis aliquet nibh in nunc sagittis mattis vel eu sem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi vitae lobortis tellus, id facilisis nunc. Praesent ut risus scelerisque libero gravida consequat. Nam vel dignissim nulla. Pellentesque semper sapien mauris, non consectetur orci tempus sed. Cras sed imperdiet est. Cras volutpat, nibh sit amet congue maximus, quam dolor efficitur massa, interdum consequat nulla tellus quis nisl. Duis vel volutpat massa.
    '''
}


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {
        'about_blog': about_blog
    })


def posts(request):
    return render(request, 'blog/posts.html')


def post(request):
    return render(request, 'blog/post.html')
