//Use this ajax-style snippet on your website alongside the discord bot to retrieve your discord status dynamically and display it on your DOM every 5 seconds
        function getOnlineStatus() {
            //Replace this link with the link to your api server, or your middleware php file
            fetch("/proxy/discordStatusRetrieve.php?discordId=213045272048041984")
                .then(async function (response) {
                    const onlineStatus = await response.text();
                    if (onlineStatus == "online" || onlineStatus == "dnd") {
                        document.querySelector("#availabilityText").innerHTML = "Recently Active";
                        document.querySelector("#availabilityText").className = "status"
                    } else if (onlineStatus == "idle") {
                        document.querySelector("#availabilityText").innerHTML = "Away";
                        document.querySelector("#availabilityText").className = "statusaway"
                    } else if (onlineStatus == "offline") {
                        document.querySelector("#availabilityText").innerHTML = "Offline";
                        document.querySelector("#availabilityText").className = "statusoffline"
                    }

                })
                .catch(function (error) {
                    document.querySelector("#availabilityText").innerHTML = "Status Unavailable";
                    document.querySelector("#availabilityText").className = "statusoffline"
                });
        }
        getOnlineStatus();
//Controls how often your status updates
        setInterval(getOnlineStatus, 5000);