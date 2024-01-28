import grpcs.message.user_pb2_grpc as user_service
import grpcs.message.user_pb2 as user_messages
from models.user import user
import grpc

passion_weights = {
    "HIP_HOP" : 1,
    "POP" : 2,
    "K_POP" : 3,
    "COFFE" : 4,
    "TIKTOK" : 5,
    "TWITTER" : 6,
}

class UserGrpcService(user_service.UserServicer):
    def getListRecommendUser(self, request, context):
        id = request.id
        ids = request.ids
        limit = request.limit
        print(id, ids, limit)

        user.load()
        if len(id)==0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("id can not null!")
            return user_messages.GetListRecommendUserResponse()
        
        existedUser = user.query(expr="id in {}".format([id]), output_fields=["embeddings"])
        if len(existedUser)==0:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("user not found!")
            return user_messages.GetListRecommendUserResponse()
        embeddings=existedUser[0].get('embeddings')

        vectors_to_search = [embeddings]
        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10},
        }
        result = user.search(vectors_to_search, "embeddings", search_params, limit, expr="id in {}".format(ids), output_fields=["id"])
        response = []
        for hits in result:
            for hit in hits:
                response.append(hit.entity.get('id'))
        user.release()
        
        return user_messages.GetListRecommendUserResponse(ids=response)
        
    def createUser(self, request, context):
        id= request.id
        sexual_orientation= request.sexual_orientation
        relationship_goal= request.relationship_goal
        passions= request.passions
        pets= request.pets
        workout= request.workout
        smoking= request.smoking
        sleeping_habit= request.sleeping_habit
        score= request.score
        print(id, score, sexual_orientation, relationship_goal, passions, request)

        if len(id)==0 or len(sexual_orientation)==0 or len(relationship_goal)==0 or len(passions)==0  :
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return user_messages.CreateUserResponse()
        
        embeddings = [
            decodeSexualOrientation(sexual_orientation), 
            decodeRelationshipGoal(relationship_goal), 
            decodePassions(passions), 
            score,
            decodePets(pets),
            decodeWorkout(workout),
            decodeSmoking(smoking),
            decodeSleepingHabit(sleeping_habit), 
        ]

        from models.user import user
        entity = {
            "id": id,
            "embeddings": embeddings
        }
        user.insert(entity)
        user.release()
        
        return user_messages.CreateUserResponse(is_success=True)
    
def decodeSexualOrientation(sexual_orientation):
        if sexual_orientation=="STRAIGHT":
            return 1
        
        if sexual_orientation=="GAY" or sexual_orientation=="LESBIAN":
            return 2
        
        if sexual_orientation=="BISEXUAL" or sexual_orientation=="ASEXUAL":
            return 3
        
        return 0
    
def decodeRelationshipGoal(relationship_goal):
    if relationship_goal=="STILL_FIGURE_OUT" or relationship_goal=="NEW_FRIEND":
        return 1
    
    if relationship_goal=="LONG_TERM_PARTNER":
        return 2
    
    if relationship_goal=="LONG_TERM_OPEN_TO_SHORT" or relationship_goal=="SHORT_TERM_OPEN_TO_LONG" or "SHORT_TERM_FUN":
        return 3
    
    return 0

def decodePassions(passions):
    code = 0
    for passion in passions:
        code+=passion_weights[passion] | 0
    return code

def decodePets(passions):
    
    return 0

def decodePassions(passions):
    
    return 0

def decodeWorkout(passions):
    
    return 0

def decodeSmoking(passions):
    
    return 0    

def decodeSleepingHabit(passions):
    
    return 0    
    
