、<html>
    
    <head>
        <title>Covid-19</title>
        
        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

        <!-- Compiled and minified JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        
        <style>
            .nav-wrapper {
                background-color: grey;
                padding-left: 20px;
            }
            
            .page-footer {
                background-color: grey;
            }
            
        </style>
        
    </head>

    <body>
        
        <nav>
            <div class="nav-wrapper">
              <a href="#" class="brand-logo"><i class="material-icons">android</i></a>
              <ul id="nav-mobile" class="right hide-on-med-and-down">
                <li><a href="sass.html">Data</a></li>
                <li><a href="badges.html">Components</a></li>
                <li><a href="collapsible.html">JavaScript</a></li>
              </ul>
            </div>
        </nav>
        
        <div class="row">
          <div class="col s12 m3 l3">
              <ul class="collection">
                <li class="collection-item avatar">
                  <img src="pikachu.jpg" alt="" class="circle">
                  <span class="title">Pikachu</span>
                  <p>Undisputed favourite pokemon <br>
                     Even grandma knows this one
                  </p>
                  <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
                </li>
                <li class="collection-item avatar">
                  <i class="material-icons circle">folder</i>
                  <span class="title">Title</span>
                  <p>First Line <br>
                     Second Line
                  </p>
                  <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
                </li>
                <li class="collection-item avatar">
                  <i class="material-icons circle green">insert_chart</i>
                  <span class="title">Title</span>
                  <p>First Line <br>
                     Second Line
                  </p>
                  <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
                </li>
                <li class="collection-item avatar">
                  <i class="material-icons circle red">play_arrow</i>
                  <span class="title">Title</span>
                  <p>First Line <br>
                     Second Line
                  </p>
                  <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
                </li>
              </ul>
          </div>
            
            
          <div class="col s12 m6 l6 orange">Map</div>
            
          <div class="col s12 m3 l3 yellow" id="mylist"></div>
            
        </div>
        
        <h1>Covid-19 Dashboard</h1>
        <p class="container">This software will provide timely info about the pandemic.</p>
        <a href="http://cnn.com" target="_blank">CNN</a><br>
        <img src="pikachu.jpg" style="width:300px; padding: 20px"> <!-- inline -->
    
        <footer class="page-footer">
          <div class="container">
            <div class="row">
              <div class="col l6 s12">
                <h5 class="white-text">Covid Dashboard</h5>
                <p class="grey-text text-lighten-4">Access the covid data you need.</p>
              </div>
              <div class="col l4 offset-l2 s12">
                <h5 class="white-text">Links</h5>
                <ul>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 1</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 2</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="footer-copyright">
            <div class="container">
            © 2020 Copyright mhoel
            <a class="grey-text text-lighten-4 right" href="#!">More Links</a>
            </div>
          </div>
        </footer>
    
    </body>
    
    <script>
        
        makelist();
        
        function makelist() {
            
            data = [{pname:"NYC",cname:"USA",conf:218000},{pname:"Moscow",cname:"Russia",conf:212000},{pname:"Sao Paulo",cname:"Brazil",conf:100000}];
            
            mylist = document.getElementById("mylist");
            
            myhtml = "<ul class='collection'>";
            for (i=0; i<data.length;i++) {
                myhtml = myhtml + "<li class='collection-item avatar'>";
                myhtml = myhtml + "<i class='material-icons circle'>folder</i>"
                myhtml = myhtml + "<b>" + data[i]['pname'] + "</b><br>";
                myhtml = myhtml + data[i]['conf'] + "</li>";
            }
            myhtml = myhtml + "</ul>";
            
            mylist.innerHTML = myhtml;
            
        }
        
    </script>

    
    
</html>
