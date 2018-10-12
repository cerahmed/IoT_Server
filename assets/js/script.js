function openDoor(elementID, elementName) {
	  if(confirm("Do you want to open " + elementName + "?")) {
		  $.ajax({
			    url: "devices/open/" + elementID,
			    type: 'GET',
			    success: function(){ 
			    	$('#successAlert').show('fade');

				    setTimeout(function(){
				      $('#successAlert').hide('fade');
//				      location.reload();
				    }, 3000);
			    },
			    error: function() {
			    	$('#failedAlert').show('fade');

				    setTimeout(function(){
				      $('#failedAlert').hide('fade');
				    }, 3000);
			    }
			});

	  }
	}