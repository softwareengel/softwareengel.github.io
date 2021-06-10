# GraphQL 

Graphql SPEC <http://spec.graphql.org/> , <http://spec.graphql.org/June2018/>


<https://graphql.org/>

<https://landscape.graphql.org/>

<https://graphql.org/learn/queries/> 

<https://graphql.org/graphql-js/mutations-and-input-types/> 

# Use GraphQL by API Tools GraphiQL


GraphiQL    https://lucasconstantino.github.io/graphiql-online/ 


GraphQL Playground <https://www.graphqlbin.com/>


## Simple GraphQL - Client and Server Apollo JS 

used by airbnb, cnbc

<https://github.com/apollographql/graphql-tools> 

<https://github.com/apollographql/apollo-server/> 

<https://www.apollographql.com/platform>

<https://www.apollographql.com/docs/apollo-server/> 

<https://www.apollographql.com/docs/tutorial/data-source/> (Add SqLite Data Source)


![Screenshot 2020 01 06 Apollo Graphql Server](../pic/Screenshot_2020-01-06-apollo-graphql-server.png)

![Screenshot 2020 01 06 Apollo Graphql Server Ui](../pic/Screenshot-2020-01-06-apollo-graphql-server-ui.png)

## Relay GraphQL Client used by FB, Github

https://www.youtube.com/watch?v=9sc8Pyc51uU 


# Neo4J

https://neo4j.com/developer/docker-run-neo4j/


    docker run \
        --name testneo4j \
        -p7474:7474 -p7687:7687 \
        -d \
        -v $HOME/neo4j/data:/data \
        -v $HOME/neo4j/logs:/logs \
        -v $HOME/neo4j/import:/var/lib/neo4j/import \
        -v $HOME/neo4j/plugins:/plugins \
        --env NEO4J_AUTH=neo4j/test \
        neo4j:latest

curl http://localhost:7474/db/data/

http://localhost:7474/webadmin/

http://localhost:7474/db/data/relationship/0

