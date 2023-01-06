var rotation_checkbox = document.querySelector("input[name=rotate_zombie]");
var membre_aleatoire_checkbox = document.querySelector("input[name=rotate_bodypart]");

let zombies = document.querySelectorAll(".zombie");
let bodyparts = document.querySelectorAll(".body-part");

rotation_checkbox.addEventListener('change', function() {
  if (this.checked) {
    // .rotate -> Make the zombie rotate
    zombies.forEach(function(zombie) {
        zombie.className = "zombie rotate";
    });
  } else {
    zombies.forEach(function(zombie) {
        zombie.className = "zombie";
    });
  }
});

membre_aleatoire_checkbox.addEventListener('change', function() {
    if (this.checked) {
        bodyparts.forEach(function(bodypart) {
            bodypart.className = "body-part";
        });
    } else {
        // .static -> Make the bodypart static
        bodyparts.forEach(function(bodypart) {
            bodypart.className = "body-part static";
        });
    }
  });