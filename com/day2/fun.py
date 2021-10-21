try:
    f = open('xyz','r')
except OSError as e:
    print e
except:
    print "Somemthing going wrong"
finally:
    print "fsdafas"
