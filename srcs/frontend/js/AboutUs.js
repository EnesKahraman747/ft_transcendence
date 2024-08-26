function showAboutUsPage() {
  const cardsData = [
    {
      imgSrc: 'src/ddyankov.jpg',
      imgAlt: 'xxx',
      firstName: 'xxx',
      lastName: 'aaaa',
    },
  ];

  const fragment = document.createDocumentFragment();

  cardsData.forEach(data => {
    const card = document.createElement('li');

    const imgDiv = document.createElement('div');
    imgDiv.classList.add('img');
    const img = document.createElement('img');
    img.src = data.imgSrc;
    img.alt = data.imgAlt;
    imgDiv.appendChild(img);
    card.appendChild(imgDiv);

    
    const nameDiv = document.createElement('div');
    nameDiv.classList.add('name');
    
    const firstNameDiv = document.createElement('div');
    firstNameDiv.textContent = data.firstName;
    nameDiv.appendChild(firstNameDiv);

    const lastNameDiv = document.createElement('div');
    lastNameDiv.textContent = data.lastName;
    nameDiv.appendChild(lastNameDiv);

    card.appendChild(nameDiv);

    
    const iconDiv = document.createElement('div');
    iconDiv.classList.add('icon-container');

    const githubBtn = document.createElement('button');
    const githubIcon = document.createElement('i');
    githubBtn.addEventListener('click', () => {
      window.open(data.githubLink, '_blank');
    });

    const linkedinBtn = document.createElement('button');
    const linkedinIcon = document.createElement('i');
    linkedinIcon.classList.add('bi', 'bi-linkedin');
    linkedinBtn.appendChild(linkedinIcon);
    linkedinBtn.addEventListener('click', () => {
      window.open(data.linkedinLink, '_blank');
    });
    iconDiv.appendChild(linkedinBtn);

    card.appendChild(iconDiv);

    fragment.appendChild(card);
  });

  const wrapper = document.querySelector('.wrapperaboutus');
  const title = document.createElement("h1");
  translateKey('ourTeam').then(ourTeamTranslation => {
    title.innerHTML = `<span id="ourTeam">${ourTeamTranslation}</span>`;
});
if (wrapper)
{
    wrapper.appendChild(title);
  const carousel = document.createElement('ul');
  carousel.classList.add('carouselaboutus');
  carousel.appendChild(fragment);


  wrapper.appendChild(carousel);
}
//translate(currentLanguage);
}
