          "use strict";
            //acá va el context que viende de django 
            //const ubicaciones = {{ context.ubicaciones }}

            function initMap() {
              const myLatLng = {lat: -27.450602,lng: -58.986801};
              const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 7,
                center: myLatLng
              });

                var marker = new google.maps.Marker({
                       position: {lat: -27.450602,lng: -58.986801},
                       map: map,
                       title: 'Resistencia',
                       draggable: true
                });

                google.maps.event.addListener(marker, 'dragend', function (event) {
                       //document.getElementById("latbox").value = this.getPosition().lat();
                       console.log('lat: '+this.getPosition().lat());
                       //document.getElementById("lngbox").value = this.getPosition().lng();
                       console.log('lng: '+this.getPosition().lng());
                });
            }