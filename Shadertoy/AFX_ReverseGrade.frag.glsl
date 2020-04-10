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
// Code original : AFX_ReverseGrade Matchbox pour Autodesk Flame

// Adapted to Natron by F.Fernandez
// Original code : AFX_ReverseGrade Matchbox for Autodesk Flame


// iChannel0: source, filter = nearest
// iChannel1: target, filter = nearest
// iChannel2: alpha, filter = nearest
// BBox: iChannel0

uniform vec3 s_whitePoint;
uniform vec3 s_blackPoint;
uniform vec3 t_whitePoint;
uniform vec3 t_blackPoint;

uniform bool premultiplied = false;


void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	
	vec2 uv = fragCoord.xy / iResolution.xy;

	vec3 source = texture2D(iChannel0, uv).rgb;
	vec3 target = texture2D(iChannel1, uv).rgb;
	float alpha	= texture2D(iChannel2, uv).r;

	vec3 result = vec3(1.0);

	if(premultiplied == true)
		if (alpha !=0.0)
			result = source / vec3(alpha);
		else
			result = vec3(0.0);

	// White Balance Source
	result 			= vec3(	(source - s_blackPoint) / s_whitePoint);
	
	// White Balance to Target Values
	result 			= vec3( (result * t_whitePoint) + t_blackPoint);

	if(premultiplied == true)
		fragColor = vec4( result*vec3(alpha), alpha);
	else
		fragColor = vec4( result, alpha);
}
