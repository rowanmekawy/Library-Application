(function(){"use strict";var e={1031:function(e,t,o){var n=o(5130),r=o(6768);function u(e,t,o,n,u,a){const i=(0,r.g2)("router-view"),l=(0,r.g2)("v-app");return(0,r.uX)(),(0,r.Wv)(l,null,{default:(0,r.k6)((()=>[(0,r.bF)(i)])),_:1})}var a={name:"App"},i=o(1241);const l=(0,i.A)(a,[["render",u]]);var c=l,s=o(1387);function f(e,t,o,n,u,a){const i=(0,r.g2)("v-icon"),l=(0,r.g2)("v-data-table"),c=(0,r.g2)("v-col"),s=(0,r.g2)("v-row"),f=(0,r.g2)("v-btn"),d=(0,r.g2)("v-container");return(0,r.uX)(),(0,r.Wv)(d,null,{default:(0,r.k6)((()=>[(0,r.bF)(s,null,{default:(0,r.k6)((()=>[(0,r.bF)(c,{cols:"12"},{default:(0,r.k6)((()=>[(0,r.bF)(l,{headers:u.headers,items:u.books,class:"elevation-1"},{["item.actions"]:(0,r.k6)((({item:e})=>[(0,r.bF)(i,{small:"",class:"mr-2",onClick:t=>a.editBook(e)},{default:(0,r.k6)((()=>[(0,r.eW)(" mdi-pencil ")])),_:2},1032,["onClick"]),(0,r.bF)(i,{small:"",onClick:t=>a.deleteBook(e._id)},{default:(0,r.k6)((()=>[(0,r.eW)(" mdi-delete ")])),_:2},1032,["onClick"])])),_:2},1032,["headers","items"])])),_:1})])),_:1}),(0,r.bF)(s,null,{default:(0,r.k6)((()=>[(0,r.bF)(c,{cols:"12"},{default:(0,r.k6)((()=>[(0,r.bF)(f,{color:"primary"},{default:(0,r.k6)((()=>[(0,r.eW)("Test Button")])),_:1}),(0,r.bF)(f,{color:"primary",onClick:a.addBook},{default:(0,r.k6)((()=>[(0,r.eW)(" Add New Book ")])),_:1},8,["onClick"])])),_:1})])),_:1})])),_:1})}var d=o(8355);const k="http://localhost:5000/api/books";class v{getAllBooks(){return d.A.get(k)}getBookById(e){return d.A.get(`${k}/${e}`)}createBook(e){return d.A.post(k,e)}updateBook(e,t){return d.A.put(`${k}/${e}`,t)}deleteBook(e){return d.A.delete(`${k}/${e}`)}}var h=new v,b={name:"BookList",data(){return{books:[],headers:[{text:"Title",value:"title"},{text:"Author",value:"author"},{text:"Genre",value:"genre"},{text:"ISBN",value:"isbn"},{text:"Actions",value:"actions",sortable:!1}]}},created(){this.fetchBooks()},methods:{fetchBooks(){h.getAllBooks().then((e=>{this.books=e.data})).catch((e=>{console.error("There was an error fetching the books:",e)}))},addBook(){},editBook(){},deleteBook(e){confirm("Are you sure you want to delete this book?")&&h.deleteBook(e).then((()=>{this.fetchBooks()})).catch((e=>{console.error("There was an error deleting the book:",e)}))}}};const p=(0,i.A)(b,[["render",f]]);var g=p;const m=[{path:"/BookList",name:"BookList",component:g}],B=(0,s.aE)({history:(0,s.LA)("/"),routes:m});var y=B,_=o(5888),w=(o(5524),(0,_.$N)({}));(0,n.Ef)(c).use(y).use(w).mount("#app")}},t={};function o(n){var r=t[n];if(void 0!==r)return r.exports;var u=t[n]={exports:{}};return e[n].call(u.exports,u,u.exports,o),u.exports}o.m=e,function(){var e=[];o.O=function(t,n,r,u){if(!n){var a=1/0;for(s=0;s<e.length;s++){n=e[s][0],r=e[s][1],u=e[s][2];for(var i=!0,l=0;l<n.length;l++)(!1&u||a>=u)&&Object.keys(o.O).every((function(e){return o.O[e](n[l])}))?n.splice(l--,1):(i=!1,u<a&&(a=u));if(i){e.splice(s--,1);var c=r();void 0!==c&&(t=c)}}return t}u=u||0;for(var s=e.length;s>0&&e[s-1][2]>u;s--)e[s]=e[s-1];e[s]=[n,r,u]}}(),function(){o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,{a:t}),t}}(),function(){o.d=function(e,t){for(var n in t)o.o(t,n)&&!o.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}}(),function(){o.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){var e={524:0};o.O.j=function(t){return 0===e[t]};var t=function(t,n){var r,u,a=n[0],i=n[1],l=n[2],c=0;if(a.some((function(t){return 0!==e[t]}))){for(r in i)o.o(i,r)&&(o.m[r]=i[r]);if(l)var s=l(o)}for(t&&t(n);c<a.length;c++)u=a[c],o.o(e,u)&&e[u]&&e[u][0](),e[u]=0;return o.O(s)},n=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))}();var n=o.O(void 0,[504],(function(){return o(1031)}));n=o.O(n)})();
//# sourceMappingURL=app.78e4c1d0.js.map