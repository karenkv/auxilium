$(document).ready(() => {

    $('#submit-btn').click(() => {
        const orgName = $('#org-name').val().trim();
        const foodChecked = $('#food-check').prop('checked');
        const hygieneChecked = $('#hygiene-check').prop('checked');
        const shelterChecked = $('#shelter-check').prop('checked');
        const address = $('#address').val().trim();
        const phoneNumber = $('#phone-number').val().trim();
        const website = $('#website').val().trim();

        let isFood = "N"
        if(foodChecked == true) {
            isFood = "Y"
        }
		
		let isHygiene = "N"
        if(hygieneChecked == true) {
            isHygiene = "Y"
        }

		isShelter = "N"
        if(shelterChecked == true) {
            isShelter = "Y"
        }

        let newOrg = {
            [orgName]: {
                "food": isFood,
				"hygiene": isHygiene,
				"shelter": isShelter,
                "website": website,
                "phone": phoneNumber,
                "name": orgName,
                "location": address
            }
        };

        console.log(newOrg);

        // i literally don't know what to do
        
        $.post('/add-new-org', {
                 "food": isFood,
				 "hygiene": isHygiene,
				 "shelter": isShelter,
                 "website": website,
                 "phone": phoneNumber,
                 "name": orgName,
                 "location": address
        }, function(data) {
            if(data === 'done') {
                console.log('hello');
                $('#confirmation-modal').show();
            }
        });
    });

});