  // Method for json for filttering
  $(document).ready(function(){    
    $.getJSON("https://aryadipura.github.io/Tugas-Besar-PPL/assets/json/Anotasi.json", function(data){
          var fashion_data = '';
          var id = 1;
          var count = 0;
          const column = 4;
          const maxColumnPerRow = 25;            
          fashion_data += "<div class="+ 'column' +">";
          $.each(data, function(key,value){
              // fashion_data += '<tr>';                
              // fashion_data += "<td><img id=" + id +" class=" + 'filterFashion' + " width='100' src="+
              //     value.image+"></td>";
              if(count == maxColumnPerRow){
                  fashion_data += "</div>";                    
                  count = 0;
                  fashion_data += "<div class="+ 'column' +">";
                  fashion_data += "<img id=" + id +" class=" + 'filterFashion' + " width='100' src="+
                  value.image+">";
                  count++;
              }else{
                  fashion_data += "<img id=" + id +" class=" + 'filterFashion' + " width='100' src="+
                  value.image+">";
                  count++; 
              }                             
              id++;
          });

          $('#fashion_image').append(fashion_data);            
      });      
      $.getJSON("https://aryadipura.github.io/Tugas-Besar-PPL/assets/json/Anotasi.json", function(data){
          var i = 1;
          $.each(data, function(key,value){
              // Add to class each label for filtering
              // TYPE
              if(value.hasOwnProperty('Type')){
                  if(value.Type.choices !== undefined){                    
                      $.each(value.Type.choices, function(k,item){
                          document.getElementById(i).classList.add(item.replace(/\s/g, ''));
                      });
                  }else{
                      document.getElementById(i).classList.add(value.Type.replace(/\s/g, ''));
                  }
              }
              

              // CLOTHES
              if(value.hasOwnProperty('Clothes')){
                  if(value.Clothes.choices !== undefined){                    
                      $.each(value.Clothes.choices, function(k,item){
                          document.getElementById(i).classList.add(item.replace(/\s/g, ''));
                      });
                  }else{
                      document.getElementById(i).classList.add(value.Clothes.replace(/\s/g, ''));
                  }
              }

              // Pants
              if(value.hasOwnProperty('Pants')){
                  if(value.Pants.choices !== undefined){                    
                      $.each(value.Pants.choices, function(k,item){
                          document.getElementById(i).classList.add(item.replace(/\s/g, ''));
                      });
                  }else{
                      document.getElementById(i).classList.add(value.Pants.replace(/\s/g, ''));
                  }
              }

              // Footwear
              if(value.hasOwnProperty('Footwear')){
                  if(value.Footwear.choices !== undefined){                    
                      $.each(value.Footwear.choices, function(k,item){
                          document.getElementById(i).classList.add(item.replace(/\s/g, ''));
                      });
                  }else{
                      document.getElementById(i).classList.add(value.Footwear.replace(/\s/g, ''));
                  }
              }

              // Accesories
              if(value.hasOwnProperty('Accecories')){
                  if(value.Accecories.choices !== undefined){                    
                      $.each(value.Accecories.choices, function(k,item){
                          document.getElementById(i).classList.add(item.replace(/\s/g, ''));
                      });
                  }else{
                      document.getElementById(i).classList.add(value.Accecories.replace(/\s/g, ''));
                  }
              }

              // Color
              if(value.hasOwnProperty('Color')){
                  if(value.Color.choices !== undefined){                    
                      $.each(value.Color.choices, function(k,item){
                          document.getElementById(i).classList.add(item.replace(/\s/g, ''));
                      });
                  }else{
                      document.getElementById(i).classList.add(value.Color.replace(/\s/g, ''));
                  }
              }
              i++;
          });
      });
  });
