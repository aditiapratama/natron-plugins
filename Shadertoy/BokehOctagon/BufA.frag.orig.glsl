const vec2 blurdir = vec2( 1.0, 0.0 );

const float blurdist_px = 64.0;
const int NUM_SAMPLES = 16;

const float THRESHOLD = 0.1;
const float MULT = 4.0;

vec3 srgb2lin(vec3 c) { return c*c; }
vec3 lin2srgb(vec3 c) { return sqrt(c); }

//note: uniform pdf rand [0;1[
float hash12n(vec2 p)
{
	p  = fract(p * vec2(5.3987, 5.4421));
    p += dot(p.yx, p.xy + vec2(21.5351, 14.3137));
	return fract(p.x * p.y * 95.4307);
}

vec4 pattern( vec2 p )
{
    float aspect = iResolution.x/iResolution.y;
    float p0 = step(abs(p.x-0.125), 0.01) * step(abs(p.y-0.27), 0.01);
    float p1 = step( length( p-vec2(0.125, 0.45) ), 0.025 );
    
    float p2_0 = step( length( p-vec2(0.08, 0.14) ), 0.0125 );
    float p2_1 = step( length( p-vec2(0.16, 0.125) ), 0.0125 );
    float p2_2 = step( length( p-vec2(0.1, 0.07) ), 0.0125 );
    float p2 = max(p2_0, max(p2_1,p2_2));
    
    return vec4( max( p0, max(p1,p2) ) );
}

vec3 sampletex( vec2 uv )
{
    float t = fract( 0.1*iGlobalTime );
    if ( t < 1.0/3.0)
    	return srgb2lin( texture2D( iChannel0, uv, -10.0 ).rgb );
    else if ( t < 2.0/3.0 )
        return srgb2lin( texture2D( iChannel1, uv, -10.0 ).rgb );
    else
	    return srgb2lin( texture2D( iChannel2, uv, -10.0 ).rgb );    
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 blurvec = normalize(blurdir) / iResolution.xx;
    fragCoord += 25.0 * vec2( cos(iGlobalTime), sin(iGlobalTime ) );
    vec2 suv = fragCoord / iResolution.xy; 
    vec2 uv = fragCoord / iResolution.xx;
    float sinblur = ( 0.55 + 0.45 * sin( 5.0 * uv.x + iGlobalTime ) );
    float blurdist = (iMouse.z>0.5) ? 100.0 * iMouse.x/iResolution.x : blurdist_px * sinblur;
    
    vec2 p0 = uv - 0.5 * blurdist * blurvec;
    vec2 p1 = uv + 0.5 * blurdist * blurvec;
    vec2 stepvec = (p1-p0) / float(NUM_SAMPLES);
    vec2 p = p0 + (hash12n(uv+fract(iGlobalTime))-0.5) * stepvec;
    
    vec3 sumcol = vec3(0.0);
    for (int i=0;i<NUM_SAMPLES;++i)
    {
        if ( suv.x < 0.25 )
            sumcol += pattern( p ).rgb;
        else
        {
            vec3 sample = (sampletex(p) - THRESHOLD) / (1.0-THRESHOLD);
            sumcol += sample*sample; //wtf
        }
        p += stepvec;
    }
    sumcol /= float(NUM_SAMPLES);
    sumcol = max( sumcol, 0.0 );
    
    fragColor = vec4( lin2srgb( sumcol * MULT ), 1.0 );
}
