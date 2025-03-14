$(function() {

    function GetSortOrder(prop) {    
        return function(a, b) {    
            if (a[prop] > b[prop]) {    
                return 1;    
            } else if (a[prop] < b[prop]) {    
                return -1;    
            }    
            return 0;    
        }    
    }   

    $("#triTitre").click(refreshMusicList);
    $("#triArtiste").click(refreshMusicListArtiste);

    function remplirMusic(musics) {
      // console.log(musics);      
      musics.sort(GetSortOrder("title"));
      // console.log(musics);

      $('#music').empty();
      $('#music').append($('<ul>'));      
      
      for(music of musics){
          // console.log(music);
          $('#music ul')
                .append($('<li>')
                .append($('<a>')
                .text(music.title)
                    ).on("click", music, details)
                );
        }
        
      }

      function remplirMusicArtiste(musics) {
      // console.log(musics);      
      musics.sort(GetSortOrder("group"));
      // console.log(musics);

      $('#music').empty();
      $('#music').append($('<ul>'));      
      
      for(music of musics){
          // console.log(music);
          $('#music ul')
                .append($('<li>')
                .append($('<a>')
                .text(music.title)
                    ).on("click", music, details)
                );
        }
        
      }

      function onerror(err) {
          $("#music").html("<b>Impossible de récupérer les musiques !</b>\n"+err);
      }

    function refreshMusicList(){
        $("#currentmusic").empty();
        requete = "http://localhost:3000/music";
        fetch(requete)
        .then( response => {
                  if (response.ok) return response.json();
                  else throw new Error('Problème ajax: '+response.status);
                }
            )
        .then(remplirMusic)
        .catch(onerror);
      }

    function refreshMusicListArtiste(){
        $("#currentmusic").empty();
        requete = "http://localhost:3000/music";
        fetch(requete)
        .then( response => {
                  if (response.ok) return response.json();
                  else throw new Error('Problème ajax: '+response.status);
                }
            )
        .then(remplirMusicArtiste)
        .catch(onerror);
      }

    function details(event){
        $("#currentmusic").empty();
        formMusic();
        fillFormMusic(event.data);
        }


    class Music{
        constructor(title, group, album, year, favori, spotify, uri){
            this.title = title;
            this.group = group;
            this.album = album;
            this.year = year;
            this.favori = favori;
            this.spotify = spotify;
            this.uri = uri;
            console.log(this.uri);
        }
    }


    $("#tools #add").on("click", formMusic);
    $('#tools #del').on('click', delMusic);

    function formMusic(isnew){
        $("#currentmusic").empty();
        $("#currentmusic")
            .append($('<span>Titre<input type="text" id="titre"><br></span>'))
            .append($('<span>Groupe<input type="text" id="group"><br></span>'))
            .append($('<span>Album<input type="text" id="album"><br></span>'))
            .append($('<span>Année<input type="text" id="year"><br></span'))
            .append($('<span>Favori<input type="checkbox" id="favori"><br></span>'))
            .append($('<span>Spotify<input type="text" id="spotify"><br></span>'))
            .append($('<button id="lien"> Lien Spotify</button>'))
            .append($('<span><input type="hidden" id="turi"><br></span>'))
            .append(isnew?$('<span><input type="button" value="Sauvegarder"><br></span>').on("click", saveNewMusic)
                         :$('<span><input type="button" value="Modifier"><br></span>').on("click", saveModifiedMusic)
                );

            $("#lien").click(openurl);
        }

    function openurl(){
        console.log($('#spotify').val());
        document.open($('#spotify').val(),"","");
    }

    function fillFormMusic(t){
        //console.log(t.spotify);
        $("#currentmusic #titre").val(t.title);
        $("#currentmusic #group").val(t.group);
        $("#currentmusic #album").val(t.album);
        $("#currentmusic #year").val(t.year);
        $("#currentmusic #spotify").val(t.spotify);
        t.favori?$("#currentmusic #favori").prop('checked', true):
        $("#currentmusic #favori").prop('checked', false);
        t.uri=(t.uri == undefined)?"http://localhost:3000/music/"+t.id:t.uri;
        $("#currentmusic #turi").val(t.uri);
        
    }

    function saveNewMusic(){
        var music = new Music(
            $("#currentmusic #titre").val(),
            $("#currentmusic #group").val(),
            $("#currentmusic #album").val(),
            $("#currentmusic #year").val(),
            $("#currentmusic #favori").is(':checked'),
            $("#currentmusic #spotify").val()
            );
        console.log(JSON.stringify(music));
        fetch("http://localhost:3000/music/",{
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify(music)
            })
        .then(res => { console.log('Save Success') ;
                       $("#result").text(res['contenu']);
                       refreshMusicList();
                   })
        .catch( res => { console.log(res) });
    }

    function saveModifiedMusic(){
        var music = new Music(
            $("#currentmusic #titre").val(),
            $("#currentmusic #group").val(),
            $("#currentmusic #album").val(),
            $("#currentmusic #year").val(),
            $("#currentmusic #favori").is(':checked'),
            $("#currentmusic #spotify").val(),
            $("#currentmusic #turi").val()
            );
        console.log("PUT");
        console.log(music.uri);
        console.log(JSON.stringify(music));
        fetch(music.uri,{
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "PUT",
        body: JSON.stringify(music)
            })
        .then(res => { console.log('Update Success'+res);  refreshMusicList();} )
        .catch( res => { console.log(res) });
    }

    function delMusic(){
        if ($("#currentmusic #turi").val()){
        url = $("#currentmusic #turi").val();
        fetch(url,{
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "DELETE"
            })
        .then(res => { console.log('Delete Success:' + res); } )
        .then(refreshMusicList)
        .catch( res => { console.log(res);  });
    }
  }
});
