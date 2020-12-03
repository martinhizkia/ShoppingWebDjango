class guessCard extends HTMLElement{

    connectedCallback() {
        this.img = this.getAttribute("imgsrc") || null;
        this.productName = this.getAttribute("name") || null;
        this.productPrice = this.getAttribute("harga") || null;
        this.url = this.getAttribute("url") || null;
        this.render();
    }
      
    render() {       
     this.innerHTML = `
     <style>
     img{
       width: 350px;
       height: 350px;}
   </style>
    <div class="col s12 m4">
    <div class="card medium">
      <div class="card-image">
        <img src="${this.img}">
      </div>
      <div class="card-content">
        <span class="card-title">${this.productName}</span>
        <p>${this.productPrice}
        </p>
      </div>
      <div class="card-action">
      <a href="${this.url}" class="waves-effect waves-light btn-small">Lihat</a>
      </div>
    </div>
    </div>
  `;}
     }
      
     customElements.define("guess-card", guessCard);