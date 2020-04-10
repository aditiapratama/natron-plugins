//
//
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//                        MM.                          .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                     MM.  .MMMM        MMMMMMM    MMM.  .MM
//                    MM.  .MMM           MMMMMM     MMM.  .MM
//                   MM.  .MmM              MMMM      MMM.  .MM
//                  MM.  .MMM                 MM       MMM.  .MM
//                 MM.  .MMM                   M        MMM.  .MM
//                MM.  .MMM                              MMM.  .MM
//                 MM.  .MMM                            MMM.  .MM
//                  MM.  .MMM       M                  MMM.  .MM
//                   MM.  .MMM      MM                MMM.  .MM
//                    MM.  .MMM     MMM              MMM.  .MM
//                     MM.  .MMM    MMMM            MMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                        MM.                          .MM
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//
//
//
//
// Adaptation pour Natron par F. Fernandez
// Code original : L_SSAO Matchbox pour Autodesk Flame

// Adapted to Natron by F.Fernandez
// Original code : L_SSAO Matchbox for Autodesk Flame


// setting inputs names and filtering options
// iChannel0:Source, filter = nearest, wrap = clamp
// iChannel1:Depth, filter = nearest, wrap = clamp
// BBox: iChannel0

/*
SSAO GLSL shader v1.2
assembled by Martins Upitis (martinsh) (devlog-martinsh.blogspot.com)
original technique is made by Arkano22 (www.gamedev.net/topic/550699-ssao-no-halo-artifacts/)

changelog:
1.2 - added fog calculation to mask AO. Minor fixes.
1.1 - added spiral sampling method from here:
(http://www.cgafaq.info/wiki/Evenly_distributed_points_on_sphere)
*/



#define PI    3.14159265359

float width = iResolution.x; //texture width
float height = iResolution.y; //texture height

vec2 texCoord = gl_TexCoord[0].st;

//------------------------------------------
//general stuff

//make sure that these two values are the same for your camera, otherwise distances will be wrong.

uniform float znear = 0.3; // Z-near : , min=0.1, max=1000
uniform float zfar = 40.0; // Z-far : , min=0.1, max=1000 


//user variables
uniform int samples = 16; // AO sample count : , min=4, max=1000

uniform float radius = 0.3; // AO radius : , min=0.01, max=100.0
uniform float aoclamp = 0.25; // Depth clamp : (reduces haloing at screen edges), min=0.01, max=10.0
uniform bool noise = true; // Use noise : (use noise instead of pattern for sample dithering)
uniform float noiseamount = 0.10; // Dithering amount : (dithering amount), min=0.0, max=100.0

uniform float diffarea = 0.4; // Self-shadowing reduction : , min=0.0, max=1.0
uniform float gdisplace = 0.4; // Gauss bell center : , min=0.0, max=1.0

uniform bool mist = true; // Use mist : 
uniform float miststart = 0.9; // Mist start : , min=0.1, max=1000.0
uniform float mistend = 1.0; // Mist end : , min=0.0, max=1000.0

uniform bool onlyAO = false; // Use only ambient occlusion pass : 
uniform float lumInfluence = 0.7; // How much luminance affects occlusion : ,min=0.0, max=1.0

//--------------------------------------------------------

vec2 rand(vec2 coord) //generating noise/pattern texture for dithering
{
	float noiseX = ((fract(1.0-coord.s*(width/2.0))*0.25)+(fract(coord.t*(height/2.0))*0.75))*2.0-1.0;
	float noiseY = ((fract(1.0-coord.s*(width/2.0))*0.75)+(fract(coord.t*(height/2.0))*0.25))*2.0-1.0;
	
	if (noise)
	{
		noiseX = clamp(fract(sin(dot(coord ,vec2(12.9898,78.233))) * 43758.5453),0.0,1.0)*2.0-1.0;
		noiseY = clamp(fract(sin(dot(coord ,vec2(12.9898,78.233)*2.0)) * 43758.5453),0.0,1.0)*2.0-1.0;
	}
	return vec2(noiseX,noiseY)*noiseamount;
}

float doMist()
{
	float zdepth = texture2D(iChannel1,texCoord.xy).x;
	float depth = -zfar * znear / (zdepth * (zfar - znear) - zfar);
	return clamp((depth-miststart)/mistend,0.0,1.0);
}

float readDepth(in vec2 coord) 
{
	if (gl_TexCoord[0].x<0.0||gl_TexCoord[0].y<0.0) return 1.0;
	return (2.0 * znear) / (zfar + znear - texture2D(iChannel1, coord ).x * (zfar-znear));
}

float compareDepths(in float depth1, in float depth2,inout int far)
{   
	float garea = 2.0; //gauss bell width    
	float diff = (depth1 - depth2)*100.0; //depth difference (0-100)
	//reduce left bell width to avoid self-shadowing 
	if (diff<gdisplace)
	{
	garea = diffarea;
	}else{
	far = 1;
	}
	
	float gauss = pow(2.7182,-2.0*(diff-gdisplace)*(diff-gdisplace)/(garea*garea));
	return gauss;
}   

float calAO(float depth,float dw, float dh)
{   
	float dd = (1.0-depth)*radius;
	
	float temp = 0.0;
	float temp2 = 0.0;
	float coordw = gl_TexCoord[0].x + dw*dd;
	float coordh = gl_TexCoord[0].y + dh*dd;
	float coordw2 = gl_TexCoord[0].x - dw*dd;
	float coordh2 = gl_TexCoord[0].y - dh*dd;
	
	vec2 coord = vec2(coordw , coordh);
	vec2 coord2 = vec2(coordw2, coordh2);
	
	int far = 0;
	temp = compareDepths(depth, readDepth(coord),far);
	//DEPTH EXTRAPOLATION:
	if (far > 0)
	{
		temp2 = compareDepths(readDepth(coord2),depth,far);
		temp += (1.0-temp)*temp2;
	}
	
	return temp;
} 

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	vec2 noise = rand(texCoord); 
	float depth = readDepth(texCoord);
	
	float w = (1.0 / width)/clamp(depth,aoclamp,1.0)+(noise.x*(1.0-noise.x));
	float h = (1.0 / height)/clamp(depth,aoclamp,1.0)+(noise.y*(1.0-noise.y));
	
	float pw;
	float ph;
	
	float ao;
	
	float dl = PI*(3.0-sqrt(5.0));
	float dz = 1.0/float(samples);
	float l = 0.0;
	float z = 1.0 - dz/2.0;
	
	for (int i = 0; i <= samples; i ++)
	{     
		float r = sqrt(1.0-z);
		
		pw = cos(l)*r;
		ph = sin(l)*r;
		ao += calAO(depth,pw*w,ph*h);        
		z = z - dz;
		l = l + dl;
	}
	
	ao /= float(samples);
	ao = 1.0-ao;	
	
	if (mist)
	{
	ao = mix(ao, 1.0,doMist());
	}
	
	vec3 color = texture2D(iChannel0,texCoord).rgb;
	
	vec3 lumcoeff = vec3(0.299,0.587,0.114);
	float lum = dot(color.rgb, lumcoeff);
	vec3 luminance = vec3(lum, lum, lum);
	
	vec3 final = vec3(color*mix(vec3(ao),vec3(1.0),luminance*lumInfluence));//mix(color*ao, white, luminance)
	
	if (onlyAO)
	{
	final = vec3(mix(vec3(ao),vec3(1.0),luminance*lumInfluence)); //ambient occlusion only
	}
	
	
	fragColor = vec4(final,1.0); 
	
}