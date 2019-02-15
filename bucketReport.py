import boto3
import sys
s3 = boto3.client('s3')
s3_report= '/home/cm/office/programs/Auto_script/s3_report.csv'
csv_file= open(s3_report,'w+')

access-key='AKIAIPKVULTEXIAQ2J7A'
Secret-access-key='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'


buckets = s3.list_buckets()
bucket_list=[]
public_acl_indicator = 'http://acs.amazonaws.com/groups/global/AllUsers'
permissions_to_check = ['READ', 'WRITE']
public_buckets = {}
for i in buckets['Buckets']:
    bucket_list.append(i['Name'])
for one_bucket in bucket_list:
    try:
        # Get bucket location
        # location = s3.get_bucket_location( Bucket=one_bucket)
        # if location['LocationConstraint'] == None:
        #     print one_bucket+"----"+'us-east-1'
        # else :
        #     print one_bucket+"----"+str(location['LocationConstraint'])
        # Get bucket Access
        bucket_acl_response = s3.get_bucket_acl(Bucket=one_bucket)
        for grant in bucket_acl_response['Grants']:
                for (k, v) in grant.iteritems():
                    if k == 'Permission' and any(permission in v for permission in permissions_to_check):
                        for (grantee_attrib_k, grantee_attrib_v) in grant['Grantee'].iteritems():
                            if 'URI' in grantee_attrib_k and grant['Grantee']['URI'] == public_acl_indicator:
                                if v not in public_buckets:
                                    public_buckets[v] = [one_bucket]
                                    print v+"---"+str(one_bucket)
                                else:
                                    public_buckets[v] += [one_bucket]
                                    print v+"---"+str(one_bucket)        
    except:
        for e in sys.exc_info():
            print e

# print public_buckets['READ']
    
    
    
    

    
    
    
    
    # # try:
    #     bucket_encryption = s3.get_bucket_encryption(Bucket=one_bucket)
    #     print one_bucket+"---\n"+str(bucket_encryption)
    # # except:
    # #     print one_bucket+str("  bucket is not accessible")
    

