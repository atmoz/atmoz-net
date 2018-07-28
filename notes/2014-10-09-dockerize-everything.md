---
tags: [docker]
---

# Dockerize everything!

I've been following the Docker project for some time now, and finally
decided to start playing with it on my own server.

## What is Docker?

Docker is designed with the analogy of shipping containers in mind. The
shipping industry has long been utilizing standard containers. They have very
specific dimensions, doors, functions and so on. So packaging and transport is
very fast and easy to do, whatever is inside the container.

The Docker team basically wanted the same for software development. An easy way
to package applications and services, so it could be shipped and deployed
anywhere.

Docker uses linux containers (LXC) to let you run programs in isolation from
your system, just like virtualization does, but without the overhead of
emulating a whole computer and OS. Instead, the containers uses the host's
kernel but has it's own libraries and filesystem. Much faster and smaller in
size.

This means that you can put your applications, with all their dependencies,
inside containers. You can run this on your laptop while developing, send
containers to your friends and let them test your application (no need for them
to customize their systems for your app to work). When you feel your
application work the way you want, you know it also work fine in production,
just upload your container and run it!

I get goosebumps just thinking about this. With proper backup of data and
containers, it would take me like 10 minutes (plus time uploading/downloading)
to redeploy all my stuff on another server on the other side of the planet. Not
to mention how faster and easier it is to develop my applications/services on
my laptop without the hassle of thinking about missing dependencies and
conflicting libraries.

## Dockerizing this blog

Let me use this blog as an example. It is just static files created by a bash
script I hacked together a while ago, so all it needs is a web server.

On hub.docker.com there is a registry of uploaded Docker images. Images are
like blueprints used by your containers. I found a simple nginx image and used
that to serve my blog.

Containers are immutable and isolated, so if you want to preserve anything or
access something external, you can mount up a volume in the container. This is
what I did with the nginx container, so it could access my webpage files.

This is how I run this blog (simplified version of `run-docker` script):

    docker run \
        --name blog_atmoz_web \
        --restart=on-failure:10 \
        -v /sites/blog.atmoz.net/http:/usr/share/nginx/html:ro \
        -e VIRTUAL_HOST=blog.atmoz.net \
        -d $@ nginx

`docker run` is called to start a container using `nginx` as image (last
parameter). I give my container a name, a restart policy (so my webpage survive
reboot), mountpoint for my static files and an environment variable telling my
proxy to use this container for incoming requests to blog.atmoz.net.

`$@` allows me to include additional parameters when developing on my laptop.
Usually I add `-p 80:80` so I can access my blog via localhost.

This was exactly the commands I used to deploy my blog for the first time:

    cd /sites
    git clone https://github.com/atmoz/blog.atmoz.net.git
    blog.atmoz.net/run-docker

Say hello to goosebumps (if you are a nerd)! :-)

Well, That's all for now. I'm still learning a lot about Docker, and recommend you do
too. If I learn something cool I will write some more later.
