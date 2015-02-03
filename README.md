# HadoopStreamPractice
Author: Weipu Zhao
## Assignment 2
Use the Hadoop Streaming API to work on the NCDC Weather data that we already used in the previous assignment. Like in the first assignment, we’ll use the following file:
/cs/bigdata/datasets/ncdc-2013-sorted.csv

###Question 5
Using the Hadoop Streaming API, write a Mapper and a Reducer that will find the maximum of the minimum daily temperatures, and the minimum of the maximum daily temperatures, for each day. We want to use a single Reducer to solve the problem. You will disregard values below -79◦C and above 59◦C as being invalid. Unfortunately, this will not remove all invalid values, consequently, some of your results may look suspicious.

1.The file starts like this: 

>AE000041196,20130101,TMAX,250,,,S,

>AG000060390,20130101,PRCP,0,,,S,

>AG000060390,20130101,TMAX,171,,,S,

>AG000060590,20130101,PRCP,0,,,S,

>AG000060590,20130101,TMAX,170,,,S,
...

2.Run my implementation of this question, mapper: NCDCMapper.py , reducer: NCDCReducer.py
The command to run is: <pre><code>hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files NCDCMapper.py,NCDCReducer.py -input assignment1q3/ncdc-2013-sorted.csv \
-output output -mapper NCDCMapper.py -reducer NCDCReducer.py
</code></pre>
3.The output starts like this:
>
- ('20130101', 'TMAX')	-49.2     
- ('20130101', 'TMIN')	31.7
- ('20130102', 'TMAX')	-50.4
- ('20130102', 'TMIN')	35.0
- ('20130103', 'TMAX')	-49.7
- ('20130103', 'TMIN')	35.6
- ('20130104', 'TMAX')	-50.6
- ('20130104', 'TMIN')	35.0
- ('20130105', 'TMAX')	-49.0
- ('20130105', 'TMIN')	40.6


###Question 6
1.The file ghcnd-countries.txt, provided with this assignment, associates country codes with countries:
>AC,Antigua and Barbuda,

>AE,United Arab Emirates,

>AF,Afghanistan

>AG,Algeria,

>AJ,Azerbaijan,
...

Again, we will use the 2013 NCDC results. We want to join the two files, so that we know the number of lines of each type of record (TMAX, TMIN, PRCP...) we have for each country. The file ghcnd-countries.txt is incomplete, you will ignore the countries that are not found in that file (or create an Unknown category for them). The Mapper will take both files as its input (you can use -input twice), and output a list of values that include all relevant values for both files (some values will be undefined, depending on which file input comes from). The output will be designed so that lines that link country codes to country names will precede all NCDC data from that country after the Shuffle/Sort phase. The reduce will merge the data, relying on the ordering of its input.

Your output file should look like this:

>- United Arab Emirates  PRCP    157
>- United Arab Emirates  TMAX    296
>- United Arab Emirates  TMIN    226
>- Algeria PRCP    1433
>- Algeria TMAX    1190
>- Algeria TMIN    1126
...

2.My implementation define map key value pair this way:

AE,0	United Arab Emirates

AE,TMAX	1

AE,TMAX	1

So the output of map will be sorted and grouped by the country name (AE) and the record type. Specifically 0 stands for the record type is the name of the country.

3.Run command: <pre><code>hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files NCDCCountryMapper.py,NCDCCountryReducer.py \
-input assignment1q3/ncdc-2013-sorted.csv -input ghcnd-countries.txt \
-output a2q1output -mapper NCDCCountryMapper.py -reducer NCDCCountryReducer.py
</code></pre>
The head of output:
>- United Arab Emirates	PRCP	157
>- United Arab Emirates	TMAX	296
>- United Arab Emirates	TMIN	226
>- Algeria	PRCP	1433
>- Algeria	TMAX	1190
>- Algeria	TMIN	1126
>- Azerbaijan	PRCP	191
>- Azerbaijan	SNWD	78
>- Azerbaijan	TMAX	3086
>- Azerbaijan	TMIN	368 
