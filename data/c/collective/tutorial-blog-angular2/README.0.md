Blog Angular 2 client
======================

Installation
------------

Install the Angular CLI globally::

    $ npm install -g angular-cli@latest

Initialize the setup::

    $ ng init

Run the client
--------------

::

    $ ng serve

You can access it by navigating to http://localhost:4200/


Material Design Lite
--------------------

Add mdl as a dependency::

  $ npm install material-design-lite --save

angular-cli.json::

  "styles": [
    "styles.css",
    "../node_modules/material-design-lite/material.css"
  ],
  "scripts": [
    "../node_modules/material-design-lite/material.js"
  ],

index.html::

  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
# Login tutorial

> Note: this tutorial goes through the different steps needed to create a basic application displaying a login form able to authentify to the Plone REST API. If you run all those steps prperly, you should obtain a code similar to the one contained in the current folder.

## Initializing the application

Create application:
```
$ ng new login
```

Add the home component:
```
$ cd login
$ ng g component home
```

As we want to be able to display either the home page, either the login page, we need routing.

Let's add two routes:

app.module.ts:

```javascript
import { RouterModule } from '@angular/router';

@NgModule({
  ...
  imports: [
    ...
    RouterModule.forRoot([
      { path: '', component: HomeComponent },
      { path: 'login', component: LoginComponent },
    ])
  ...
})
```

app.component.html:
```html
<nav>
  <a routerLink="/">Home</a>
  <a routerLink="/login">Login</a>
</nav>
<router-outlet></router-outlet>
```

## Initializing the Login component

Add the login component:
```
$ ng g component login
```

A `./login` folder has been created containing the component `.ts` file, its `.css` style file, its `.html` template, and its `.spec.ts` test file.

## Implementing the Lofin service
We prefer to implement the logic logic outside the component itself (which is supposed to focus only on the UI aspects).

We need an extra file here to implement the login service.

Go in the `./login` folder and create a `login.service.ts` file:

```javascript
import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from "rxjs/Observable";
import "rxjs/add/operator/map";

@Injectable()
export class UserService {
  private loggedIn = false;

  constructor(private http: Http) {
    this.loggedIn = !!localStorage.getItem('auth_token');
  }

  login(login: string, password: string): Observable<any> {
    // let backend = 'http://localhost:8080/Plone'; // Plone 5
    let backend = 'http://localhost:8080/Plone'; // plone.server
    let headers = new Headers();
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');

    return this.http.post(
      backend + '/@login',
      JSON.stringify({
        'login': login,
        'password': password
      }),
      { headers }
    )
    .map(res => res.json())
    .map((res) => {
 
      if (res.token) {
        localStorage.setItem('auth_token', res.auth_token);
        this.loggedIn = true;
      }

      return true;
    });
  }

  logout() {
    localStorage.removeItem('auth_token');
    this.loggedIn = false;
  }

  isLoggedIn() {
    return this.loggedIn;
  }
}
```

It provides a `login()` method which returns an observable (all HTTP calls are handled as observables in Angular 2, so we can subscibe to them, and take an action when we get a response).

We can use the `map()` method on observables in order to chain different transformation or processing, and each `map()` call will also return an observable.

In our current case, we parse the JSON returned by the backend, then we check if it contains a token, and if that is the case, it stores it in the localstorage.

It also provides a `logout()` method to remove the stored token.

## Using the service in the component

Now we can use our service in our Login component:

login/login.component.ts:
```javascript
...
import { UserService } from './login.service';

@Component({
  ...
  providers: [UserService],
})
export class LoginComponent implements OnInit {

  loggedIn = false;
  authentication_error = false;

  constructor(private userService: UserService, private router: Router) {}

  ngOnInit() {
    this.loggedIn = this.userService.isLoggedIn();
  }

  logout() {
    this.userService.logout();
    this.router.navigate(['']);
  }

  onSubmit(form) {
    this.userService.login(form.username, form.password).subscribe(
      data => {
        if (data===true) {
          this.router.navigate(['']);
        }
      },
      err => {
        this.authentication_error = true;
        console.log("Can't get page. Error code: %s, URL: %s ",
                err.status, err.url);
       }
    );
  }
}
```

We make the service accessible from our component by declaring it in the `providers` list, and by adding it as a parameter in the constructor.

> We do not need to add the routing service in `providers` because it is already provided at a global level (in `app.module.ts`), but we do it to mention it the constructor so we can access it from the component implementation.

In the `onSubmit` method, we call the service's `login` method, and we subscribe to the returned observable. Depending on the answer, we will either redirect to the home page or display an error message.

The Login component template will just display a form that way:

login/login.component.html:
```html
<div [hidden]="!loggedIn">
  You are logged in. <button (click)="logout()">Logout</button>
</div>
<form #f="ngForm" (ngSubmit)="onSubmit(f.value)">
  <div [hidden]="!authentication_error">
    Authentication failed!
  </div>
  <div>
    <label for="username">Username</label>
    <input type="text" name="username"  id="username" required ngModel />
  </div>
  <div>
    <label for="password">Password</label>
    <input type="password" name="password" id="password"
    required ngModel />
  </div>
  <button>
    Log in
  </button>
</form>
```

As in the Search tutorial, the form element binds its submit event to the `onSubmit` method we created in the component using the `(ngSubmit)` directive, and the input elements are bound to the form using the `ngModel` directive.

We also make sure to display (or not) the error message and the Logout button depending on the current state of the component using the `[hidden]` directive.

We bind the `logout()` method to the button click using the `(click)` directive.

We can now launch the app:

```
$ ng serve
```
Then go to http://localhost:4200 in your browser.# Blogpost tutorial

> Note: this tutorial goes through the different steps needed to create a basic application with the following features: displaying a list of blog posts, displaying a detailed blog post, and creating a new post. If you run all those steps properly, you should obtain a code similar to the one contained in the current folder.

## Initializing the application

Create application:
```
$ ng new blogpost
```

Add the home component:
```
$ cd blogpost
$ ng g component home
```

As we want to be able to display either the home page, either the post creation page, either the post detail page, we will need 3 routes. But for now we will only use one route for home.

Instead of declaring our routes directly in the app module, we will create a specific file:

app.routes.ts:

```javascript
import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  { path: '', component: HomeComponent }
];

export const appRoutingProviders: any[] = [];

export const routing: ModuleWithProviders = RouterModule.forRoot(routes);
```

As you can see, the last route uses a parameter which will allow us to specifiy the post id in the path.

And we load our routes in the module like this:
app.module.ts:

```javascript
  import { RouterModule } from '@angular/router';
  import {
    routing,
    appRoutingProviders
  } from './app.routes';

  @NgModule({
    ...
    imports: [
      ...
      RouterModule,
      routing
    ],
    providers: [
      ...,
      appRoutingProviders
    ]
  })
```

app.component.html:
```html
  <nav>
    <a routerLink="/">Home</a>
  </nav>
  <router-outlet></router-outlet>
```

# Displaying the list of posts

The list of posts will be displayed by the Home component.

First, we need a service to fetech all the posts from the Plone backend:

home/home.service.ts:
```javascript
import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

@Injectable()
export class HomeService {

  constructor(private http: Http) {}

  getBlogPosts(): Observable<any> {
    let backend = 'http://localhost:8080/Plone'; // Plone 5
    // let backend = 'http://localhost:8080/Plone'; // plone.server
    let headers = new Headers();
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Bearer ' + localStorage.getItem('auth_token'));

    return this.http.get(backend + '/news', { headers })
    .map(res => res.json().items)
    .map(res => {
      return res
      .filter(item => item['@type'] === 'News Item')
      .map(item => {
        let parts = item['@id'].split('/');
        item.postId = parts[parts.length - 1];
        return item;
      });
    });
  }
}
```

This service has a unique method which makes a GET on the backend's `/news` folder.
The results are:

- firstly, filtered in order to get only News Items
  
  > It would have been more accurate to ask the backend to perform this filtering using the `@search` endpoint but that is not in the scope of this tutorial.

- secondly, processed in order to set an id on our retrieved posts (we use the last part of the `@id` attributes which contains the URL of the post).

In the Home component, we instantiate the service using `providers`, and we inject it in the constructor. Now we can subscribe to it and get the blogposts list:

home/home.component.ts:
```javascript
import { Component, OnInit } from '@angular/core';
import { HomeService } from './home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [HomeService]
})
export class HomeComponent implements OnInit {

  blogPosts: any;

  constructor(private homeService: HomeService) { }

  ngOnInit() {
    this.homeService.getBlogPosts().subscribe( res => {
      this.blogPosts = res;
    });
  }
}

```
To display the posts, we do a loop using `*ngFor`:

home/home.component.html:
```
<button [routerLink]="['/create']">
Create Blog Post
</button>
<div *ngFor="let blogPost of blogPosts">
  <h2>{{blogPost.title}}</h2>
  <div>
    {{blogPost.description}}
  </div>
  <a [routerLink]="blogPost.postId">
    Continue reading...
  </a>
</div>
```
As you can see, the links to the detailed posts and the link to the Create button are managed by the router (using the `routerLink` directive). We will declare the needed routes later.

## Displaying a detailed post

Add the blogpost component:
```
$ ng g component blogpost
```

Add a route to call the Blogpost component:

app.routes.ts:

```javascript
...
import { BlogpostComponent } from './blogpost/blogpost.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: ':path', component: BlogpostComponent }
];
...
```
As you can see, our new route uses a parameter which will allow us to specifiy the post id in the path. For instance http://localhost:4200/plone-rocks will display the post which id is `plone-rocks`

We also need a service to call the backend, we create a new file named blogpost/blogpost.service.ts:
```javascript
import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

@Injectable()
export class BlogPostService {

  backend = 'http://localhost:8080/Plone'; // Plone 5
  // backend = 'http://localhost:8080/Plone'; // plone.server

  constructor(private http: Http) {}

  getBlogPost(id): Observable<any> {
    let headers = new Headers();
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Bearer ' + localStorage.getItem('auth_token'));

    return this.http.get(this.backend + '/news/' + id, { headers })
    .map(res => res.json());
  }
}

```

Now we can implement the component:

blogpost/blogpost.component.ts:
```javascript
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BlogPostService } from './blogpost.service';

@Component({
  selector: 'app-blogpost',
  templateUrl: './blogpost.component.html',
  styleUrls: ['./blogpost.component.css'],
  providers: [BlogPostService]
})
export class BlogpostComponent implements OnInit {

  blogpostId: string;
  title: string;
  description: string;
  text: string;

  constructor(
    private route: ActivatedRoute,
    private blogPostService: BlogPostService) {
  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      let path = params['path'];
      this.blogPostService.getBlogPost(path).subscribe(item => {
        this.title = item.title;
        this.description = item.description;
        this.text = item.text.data;
      });
    });
  }
}

```

By injecting `ActivatedRoute` in our constructor (note: we do not need to add it to the `providers` list, it is provided at the app global level), we can subscribe to the route `params`, so we can get the post id requested in the current path.

The template is very simple:

blogpost/blogpost.component.html:
```html
<h2>{{title}}</h2>
<div>{{description}}</div>
<p [innerHTML]="text"></p>
```
> Note: we use the `innerHTML` directive so the `text` value is rendered as HTML.

## Creating a new post

We will not generate a component folder for the post creation, we will just implement it in the existing `./blogpost` folder.

We add a new method in blogpost/blogpost.service.ts:
```javascript
...
@Injectable()
export class BlogPostService {
  ...

  postBlogPosts(title, description, text): Observable<any> {
    let headers = new Headers();
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Bearer ' + localStorage.getItem('auth_token'));

    return this.http.post(
      this.backend + '/news',
      JSON.stringify({
        '@type': 'News Item',
        'title': title,
        'text': text,
        'description': description,
      }),
      { headers })
    .map(res => res.json())
    .map((res) => {
      return true;
    });
  }
}
```
It makes a POST request in the Plone `/news` folder to create a new "News Item" content. It returns `true` if the creation is successful.

We create blogpost/blogpost.create.component.ts:
```javascript
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { BlogPostService } from './blogpost.service';

@Component({
  selector: 'app-home',
  templateUrl: './blogpost.create.component.html',
  styleUrls: ['./blogpost.component.css'],
  providers: [BlogPostService]
})
export class BlogpostCreateComponent {

  constructor(private blogPostService: BlogPostService, private router: Router) {}

  onSubmit(form) {
    this.blogPostService.postBlogPosts(form.title, form.description, form.text).subscribe(
      data => {
        if (data === true) {
          this.router.navigate(['']);
        }
      },
      () => console.log('Done')
    );
  }

}

```
The `onSubmit` will call the service to create the post, and then redirect to home.

Now we need to declare this new component in the app module:

app.module.ts:
```javascript
...
import { BlogpostCreateComponent } from './blogpost/blogpost.create.component';

@NgModule({
  declarations: [
    ...
    BlogpostCreateComponent
  ],
  ...
```

And we need to declare its route:

app.routes.ts:

```javascript
...
import { BlogpostCreateComponent } from './blogpost/blogpost.create.component';

export const routes: Routes = [
  ...
  { path: 'create', component: BlogpostCreateComponent }
];
...
```

We can now launch the app:

```
$ ng serve
```
Then go to http://localhost:4200 in your browser.
# Search tutorial

> Note: this tutorial goes through the different steps needed to create a basic search application based on the Plone REST API. If you run all those steps prperly, you should obtain a code similar to the one contained in the current folder.

## Initialize the application

Cd to your project directory and use ng to create a new search application:
```
$ ng new search
```

This will bootstrap a basic package together in a directory named after the
application. In our case, search.  Finally we will add a search component.

Cd into the newly created search directory and use ng to create the component:
```
$ cd search
$ ng g component search
```

The new search component should live in the the app container. Cd into the component:
```
$ cd ./src/app/search
```

The following files should have been generated for you:
```
search.component.css
search.component.html
search.component.spec.ts
search.component.ts
```

You'll see that the component in search.component.ts defines its css selector, css and html template files:

```javascript
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
    })
```

The `selector` indicates the tagname we can use to include this component somewhere (and we will include it in the app main template later).

## Adding the Search Template

Open the `search.component.html` file in a text editor and remove the default html generated during bootstrap.

Add the following html to the file:

```html
<form #f="ngForm" (ngSubmit)="onSubmit(f.value)">
  <div>
    <label for="search">Search Site</label>
    <input type="text" name="search" id="search" ngModel />
  </div>
  <button>Search</button>
  <ol>
    <li *ngFor="let item of items">{{ item.title }}</li>
  </ol>
</form>
```

Here is what it does:

  - the `#f="ngForm"` directive indicates we create a local variable (named `f`) to handle the current NgForm object,
  - the `ngSubmit` directive allows to bind the submit event to any method (here the `onSubmit` method that will be implemented later in our component),
  - the `ngModel` directive on the `input` tag add the input value to the form model (basically, it means `f.value` will contain a property named `search` containing the current value of our input),
  - and finally, the `ngFor` directive allows to loop over the `items` values to display the results, `items` is a property of our component (and we will set its value according the backend response).

## Implementing the component

Open the `search.component.ts` file in a text editor and modfiy it that way:

```javascript
import { Component, OnInit } from '@angular/core';
import { Http, Headers } from '@angular/http';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  items = []

  constructor(private http: Http) { }

  ngOnInit() {}

  onSubmit(form) {
    let backend = 'http://localhost:8080/Plone'; // Plone 5
    // let backend = 'http://localhost:8080/Plone'; // plone.server
    let headers = new Headers();
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');

    let query = '?SearchableText=' + form.search;

    return this.http.get(
      backend + '/@search' + query,
      { headers }
    )
    .subscribe(res => {
      let data = res.json();
      this.items = data.items;
    })
  }
}
```

> Make sure to comment/uncomment the proper backend definition.

Explanations:

  - we declare our `items` property as an empty array,
  - we inject the `Http` service in the constructor so we can use it locally,
  - we implement the `onSubmit` method that will be called when the user will submit the form:
    - it creates an HTTP GET request to the Plone API `@search` entry point using the `SearchableText` index,
    - we subscribe to this HTTP request, so we can process its returned value once returned,
    - we parse it as JSON,
    - and put its `items` property in our component's `items` property.

## Displaying the component in the app

Finally we need to insert our Search component in the main app template.

Open the `search.component.html` file in a text editor and replace the default html generated during bootstrap with:

```html
<app-search></app-search>
```

We can now launch the app:

```
$ ng serve
```
Then go to http://localhost:4200 in your browser.