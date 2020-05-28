---
layout: post
title: mongo redis   
categories: [db]
tags: [db, mongo, redis]
--- 

# Database 

# Mongo 

<https://www.mongodb.com/mongodb-3.6>

## Docker install 

    $ mkdir -p ~/data/mongo

    $ docker run \
    --name my-mongo \
    -p 27017:27017 \
    -v ~/data/mongo:/data/db \
    -d mongo

## mongo cli 

    docker run \
    -it --rm \
    --link my-mongo:mongo \
    mongo \
    sh -c 'exec mongo --host mongo'

### commands 

    db.enableFreeMonitoring()

Startup -aus Zip: 
 
    mongod --dbpath ./data

Operators in Queries:  <https://docs.mongodb.com/manual/reference/operator/query/>

## Mogo Tutorials 

<https://mkyong.com/tutorials/java-mongodb-tutorials/> 

SQL - Mongo Mapping chart 

<https://docs.mongodb.com/manual/reference/sql-comparison/>

## c client 

<https://docs.mongodb.com/ecosystem/drivers/c/> 

## java client 


    // 1. The database for reactive, real-time applications
    MongoClient mongoClient;

    // Create a new MongoClient with a MongoDB URI string.
    if (args.length == 0) {
    // Defaults to a localhost replicaset on ports: 27017, 27018, 27019
      mongoClient = new MongoClient(new
      MongoClientURI("mongodb://localhost:27017,localhost:27018,localhost:27019"));
    } else {
      mongoClient = new MongoClient(new MongoClientURI(args[0]));
    }

    // Select the MongoDB database.
    MongoDatabase database = mongoClient.getDatabase("testChangeStreams");

    // Select the collection to query.
    MongoCollection collection = database.getCollection("documents");

    // Create the change stream cursor.
    MongoCursor> cursor = collection.watch().iterator();

# Redis 

## Java Client Geo Search 

<https://gist.github.com/samklr/dee192f0cde5f322cc2a>



    import java.util.*;
    import com.lambdaworks.redis.*;

    public class LettuceGeoDemo {

        public static void main(String[] args) {

            RedisClient redisClient = new RedisClient("localhost", 6379);
            RedisConnection<String, String> redis = redisClient.connect();
            String key = "my-geo-set";

            redis.geoadd(key, 8.6638775, 49.5282537, "Weinheim", 8.3796281, 48.9978127, "Office tower", 8.665351, 49.553302,
                    "Train station");

            Set<String> georadius = redis.georadius(key, 8.6582861, 49.5285695, 5, GeoArgs.Unit.km);
            System.out.println("Geo Radius: " + georadius);

            // georadius contains "Weinheim" and "Train station"

            Double distance = redis.geodist(key, "Weinheim", "Train station", GeoArgs.Unit.km);
            System.out.println("Distance: " + distance + " km");

            // distance ≈ 2.78km

            GeoArgs geoArgs = new GeoArgs().withHash().withCoordinates().withDistance().withCount(2).asc();

            List<GeoWithin<String>> georadiusWithArgs = redis.georadius(key, 8.665351, 49.5285695, 5, GeoArgs.Unit.km, geoArgs);

            // georadiusWithArgs contains "Weinheim" and "Train station"
            // ordered descending by distance and containing distance/coordinates
            GeoWithin<String> weinheim = georadiusWithArgs.get(0);

            System.out.println("Member: " + weinheim.member);
            System.out.println("Geo hash: " + weinheim.geohash);
            System.out.println("Distance: " + weinheim.distance);
            System.out.println("Coordinates: " + weinheim.coordinates.x + "/" + weinheim.coordinates.y);

            List<GeoCoordinates> geopos = redis.geopos(key, "Weinheim", "Train station");
            GeoCoordinates weinheimGeopos = geopos.get(0);
            System.out.println("Coordinates: " + weinheimGeopos.x + "/" + weinheimGeopos.y);

            redis.close();
            redisClient.shutdown();
        }
    }