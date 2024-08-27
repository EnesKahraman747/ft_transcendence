function showAboutUsPage() {
  const cardsData = [
    {
      imgSrc: 'src/we.png',
      imgAlt: '',
      firstName: 'Hüseyin Öner - Mustafa Saydam - Bengisu Kayan - Enes Kahraman',
      lastName: '42 Ping Pong Projesi 23.06.2024 - 27.08.2024',
      
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
